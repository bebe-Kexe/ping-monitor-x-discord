import time
from ping3 import ping 
import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
import sys

if os.path.exists(".env_vars"):
    pass
else:
    with open(".env_vars", "w") as f:
        f.write("DISCORD_TOKEN=xxx.yyy.zzz\nCHANNEL_ID=1234567890\nUSER_ID=1234567890\nHOST_TO_PING=google.com\nPING_INTERVAL=5\nPING_THRESHOLD=120\n")
        print("\n.env_vars file created\n")
        print("Please fill in the .env_vars file with the required information\n")
        sys.exit()
        
load_dotenv(".env_vars")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
USER_ID = os.getenv("USER_ID")
HOST_TO_PING = os.getenv("HOST_TO_PING")
PING_INTERVAL = int(os.getenv("PING_INTERVAL"))
PING_THRESHOLD = int(os.getenv("PING_THRESHOLD"))

high_ping_notifies = False 

class PingMonitor:
    async def get_username_from_id(self, user_id):
        try:
            user = await self.client.fetch_user(int(user_id))
            return user.name
        except Exception as e:
            print(f"Error fetching username: {e}")
            return "User"



    def __init__(self):
        intents = discord.Intents.default()
        self.client = commands.Bot(command_prefix="?", intents=intents)
        self.high_ping_start_time = None
        self.normal_ping_start_time = None
        self.username = None
        
        ping_monitor = self

        @self.client.event
        async def on_ready():
            print(f'\nLogged in as {self.client.user}')

            try:
                await self.client.tree.sync()
                print("\nSlash commands synced")
            except Exception as e:
                print(f"\nError while syncing slash commands: {e}")

            if USER_ID:
                self.username = await self.get_username_from_id(USER_ID)
            else:
                self.username = "User"

            await self.client.change_presence(activity=discord.Activity(
                type = discord.ActivityType.watching,
                name = f"ping for @{self.username}"
            ))
            await self.start_monitoring()

        @self.client.tree.command(
                name="test_message", 
                description="Sends a test message so you know how alert message looks like.",
                )
        async def test(interaction: discord.Interaction):
            try:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                ping_time = await ping_monitor.check_ping()
                user_mention = f"<@{USER_ID}>" if USER_ID else f"@{self.username}"

                embed = discord.Embed(
                    title="⚠️ High Ping Alert",
                    description=f"High ping detected to {HOST_TO_PING} {user_mention}",
                    color=discord.Color.red()
                )

                embed.add_field(name="Current Ping", value=f"{ping_time:.2f} ms", inline=False)
                embed.add_field(name="Threshold", value=f"{PING_THRESHOLD} ms", inline=False)
                embed.add_field(name="Time", value=current_time, inline=False)
                embed.set_footer(text="This is a test message")

                await interaction.response.send_message(embed=embed, ephemeral=True)
                print("\nCommand response sent successfully\n")
            except Exception as e:
                print(f"\nError while sending command response: {e}\n")
                try:
                    await interaction.response.send_message(f"Error while sending command response {e}", ephemeral=True)
                except:
                    pass

        
        @self.client.tree.command(
            name="clear",
            description="Clear a specific number of messages. Note that messages older than 14 days are going to be deleted really slowly and you may encounter an error."
            )
        @app_commands.describe(amount="Number of messages to clear (1-100)")
        async def clear(interaction: discord.Interaction, amount: int):
            try:
                if amount <= 0 or amount > 100:
                    await interaction.response.send_message("Please provide a number between 1 and 100", ephemeral=True)
                    return
                    
                await interaction.response.defer(ephemeral=True)
                
                if not isinstance(interaction.channel, discord.TextChannel):
                    await interaction.followup.send("This command can only be used in text channels", ephemeral=True)
                    return
                    
                if not interaction.channel.permissions_for(interaction.guild.me).manage_messages:
                    await interaction.followup.send("I don't have permission to manage messages in this channel", ephemeral=True)
                    return
                
                deleted_count = 0

                def is_deletable(msg):
                    nonlocal deleted_count
                    if deleted_count < amount:
                        deleted_count += 1
                        return True
                    return False
                    
                await interaction.followup.send(f"Deleting {amount} messages... Note that messages older than 14 days will delete slowly and you may encounter an error.", ephemeral=True)
                deleted = await interaction.channel.purge(limit=amount, check=is_deletable)

                await interaction.followup.send(f"Successfully cleared {len(deleted)} messages", ephemeral=True)
                print(f"\nSuccessfully cleared {len(deleted)} messages\n")
                
            except discord.errors.Forbidden:
                await interaction.followup.send("I don't have permission to delete messages", ephemeral=True)
                print("\nError: Missing permissions to delete messages\n")
                
            except Exception as e:
                print(f"\nError while clearing messages: {e}\n")
                try:
                    await interaction.followup.send(f"Error while clearing messages: {e}", ephemeral=True)
                except:
                    pass
            


    async def set_high_ping_status(self):
        await self.client.change_presence(
            activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"@{self.username} experience high ping"
            ),
            status=discord.Status.dnd
        )
    
    async def set_normal_ping_status(self):
        await self.client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"ping for @{self.username}"
            ),
            status=discord.Status.online
        )
        

    async def setup(self): 
        pass

    async def start_monitoring(self):
        print (f"\nStarting ping monitoring to {HOST_TO_PING} every {PING_INTERVAL} seconds")
        print (f"\nNotification threshold is {PING_THRESHOLD} ms\n")

        current_time = time.time()
        self.high_ping_start_time = None
        self.normal_ping_start_time = None

        while True:
            ping_time = await self.check_ping()

            if ping_time is not None:
                current_time = time.time()
                print(f"Current ping: {ping_time:.2f}ms")

                if ping_time > PING_THRESHOLD:
                    self.normal_ping_start_time = None
                    global high_ping_notifies

                    if not high_ping_notifies:
                        await self.send_notifications(ping_time)
                        await self.set_high_ping_status()
                        high_ping_notifies = True
                        print(f"High ping detected: {ping_time:.2f}ms")
                else:
                    self.high_ping_start_time = None
                    if high_ping_notifies:
                        if self.normal_ping_start_time is None:
                            self.normal_ping_start_time = current_time
                        if current_time - self.normal_ping_start_time >= 5:
                            print("Ping returned to normal levels")
                            await self.set_normal_ping_status()
                            high_ping_notifies = False
                            self.normal_ping_start_time = None
        
            await asyncio.sleep(PING_INTERVAL)

    async def check_ping(self):
        try:
            result = ping(HOST_TO_PING, timeout=2)
            if result is not None:
                return result*1000
            else:
                print(f"\nFailed to ping {HOST_TO_PING}\n")
                return None
        except Exception as e:
            print(f"\nError while pinging: {e}\n")
            return None
    
    async def send_notifications(self, ping_time):
        try:
            channel = self.client.get_channel(CHANNEL_ID)

            if channel is None:
                print(f"\nError: Could not find Discord channel with ID {CHANNEL_ID}\n")
                return
        
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            user_mention = f"<@{USER_ID}>" if USER_ID else f"@{self.username}"

            embed = discord.Embed(
                title="⚠️ High Ping Alert",
                description=f"High ping detected to {HOST_TO_PING}",
                color=discord.Color.red()
            )

            embed.add_field(name="Current Ping", value=f"{ping_time:.2f} ms", inline=False)
            embed.add_field(name="Threshold", value=f"{PING_THRESHOLD} ms", inline=False)
            embed.add_field(name="Time", value=current_time, inline=False)

            await channel.send(user_mention, embed=embed)

        except Exception as e:
            print(f"\nError sending discord notification: {e}\n")


    async def run(self):
        await self.setup()
        print(f"Registered commands: {[cmd.name for cmd in self.client.tree.get_commands()]}")
        await self.client.start(DISCORD_TOKEN)

if __name__ == '__main__':
    monitor = PingMonitor()
    asyncio.run(monitor.run())