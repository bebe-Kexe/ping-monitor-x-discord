import time
from ping3 import ping 
import discord
import asyncio
import os
from dotenv import load_dotenv

if os.path.exists(".env_vars"):
    pass
else:
    os.create(".env_vars")
    with open(".env_vars", "w") as f:
        f.write("DISCORD_TOKEN=\nCHANNEL_ID=\nUSER_NAME=")
        print("Please fill in the .env_vars file with the required information")

load_dotenv(".env_vars")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
USER_NAME = os.getenv("USER_NAME")

HOST_TO_PING = 'google.com'
PING_INTERVAL = 5
PING_THRESHOLD = 120

high_ping_notifies = False 

class PingMonitor:
    def __init__(self):
        self.client = discord.Client(intents=discord.Intents.default())
        
        
        @self.client.event
        async def on_ready():
            print(f'Logged in as {self.client.user}')
            await self.start_monitoring()

    async def setup(self): 
        pass

    async def start_monitoring(self):
        print (f"Starting ping monitoring to {HOST_TO_PING} every {PING_INTERVAL} seconds")
        print (f"Notification threshold is {PING_THRESHOLD} ms")

        while True:
            ping_time = await self.check_ping()

            if ping_time is not None:
                print(f"Current ping: {ping_time:.2f}ms")

                if ping_time > PING_THRESHOLD:
                    global high_ping_notifies
                    if not high_ping_notifies:
                        await self.send_notifications(ping_time)
                        high_ping_notifies = True
                        print(f"High ping detected: {ping_time:.2f}ms")
                    else:
                        if high_ping_notifies:
                            print("Ping returned to normal levels")
                            high_ping_notifies = False
        
            await asyncio.sleep(PING_INTERVAL)

    async def check_ping(self):
        try:
            result = ping(HOST_TO_PING, timeout=2)
            if result is not None:
                return result*1000
            else:
                print(f"Failed to ping {HOST_TO_PING}")
                return None
        except Exception as e:
            print(f"Error while pinging: {e}")
            return None
    
    async def send_notifications(self, ping_time):
        
        try:
            channel = self.client.get_channel(CHANNEL_ID)

            if channel is None:
                print(f"Error: Could not find Discord channel with ID {CHANNEL_ID}")
                return
        
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            embed = discord.Embed(
                title="⚠️ High Ping Alert",
                description=f"High ping detected to {HOST_TO_PING}",
                color=discord.Color.red()
            )

            embed.add_field(name="Current Ping", value=f"{ping_time:.2f} ms", inline=False)
            embed.add_field(name="Threshold", value=f"{PING_THRESHOLD} ms", inline=False)
            embed.add_field(name="Time", value=current_time, inline=False)

            await channel.send(embed=embed)

        except Exception as e:
            print(f"Error sending discord notification: {e}")


    async def run(self):
        await self.setup()
        if high_ping_notifies == True:
            self.client.activity = discord.Activity(type=discord.ActivityType.watching, name=f"@{USER_NAME} is currently on a high ping")
            await asyncio.sleep(5)
        else:
            self.client.activity = discord.Activity(type=discord.ActivityType.watching, name=f"ping for @{USER_NAME}")
        await self.client.start(DISCORD_TOKEN)

if __name__ == '__main__':
    monitor = PingMonitor()
    asyncio.run(monitor.run())