<h1 align="center">Ping Monitor with Discord Notifications</h1>

A Python-based utility that monitors your network ping in real-time and sends alerts to Discord when latency exceeds a specified threshold.

<p align="center">
  <img src="https://media.discordapp.net/attachments/1019689698584690710/1344670229413892107/5f30XFiOJ5aa2uxWJtW1394hrwmwDT5JdPCbIEtaoid7NLOWZhv9wkWCCoAQMxrarmlceEtyhuGaRlDxtUmlsrC9wU8SfJ1V46Qmr6pnBHHZd6daThgEOUKT2luW1a864sir8am5sLhTuQ6hHyFEHgVEs6Hc2FoPD9gQdSaIN6TJb7ldTHxGCVM5rUNFD5.png?ex=67c1c13d&is=67c06fbd&hm=08a9a3b5bc9962838d28694033d5fb0153fb29b4270c43c826ce3584539fc3b5&="alt="Discord Notification Example">
</p>

<p align="center">
  <span style="color:red;">Made this out of boredom from high ping, which made me rage in competitive games.</span>
</p>

<p align="center">
  <span;">Total time spent on this project:</span>
</p>
<p align="center">
  <a href="https://wakatime.com/badge/github/bebe-Kexe/ping-monitor-x-discord?style=for-the-badge"><img src="https://wakatime.com/badge/github/bebe-Kexe/ping-monitor-x-discord.svg" alt="wakatime"></a>
</p>

## 🌟 Features

- **Real-time ping monitoring** to a specified host
- **Discord notifications** when ping exceeds the threshold
- **Custom status** on your Discord bot showing your current ping condition
- **Configurable** to match your needs
- **User-friendly** setup and startup scripts

## 📋 Requirements

- Python 3.11+ (recommended)
- Discord bot token and permissions
- Internet connection


1. Download [**LATEST RELEASE**](https://github.com/bebe-Kexe/ping-monitor-x-discord/releases).zip (always called after the version you have downloaded)
   - Unzip it into your desired directory

2. Install dependencies:
   - Open the ``ping-monitor-x-discord`` folder
   - Simply double-click ``setup.bat``

## 💻 Usage

Run the script with:

- Double-click ``start.bat``
  - If this is your first time running it, a ``.env_vars`` file will be created. Open it with a text editor and specify ``DISCORD_TOKEN``, ``CHANNEL_ID``, and ``USER_ID`` (optional).

## 💻 Usage

Run the script with:

```.env_vars
DISCORD_ENABLED=True #If you want to have discord features enabled (default true)

# (DISCORD_ENABLED must be set to 'true' for these features to work!)
DISCORD_TOKEN=xxx.yyy.zzz  #Replace with your bot token 
CHANNEL_ID=1234567890      # Replace with channel ID
USER_ID=1234567890         # Replace with your username (optional)
DISCORD_USER_MENTION=True  #If the bot mentions you in alert message (default true)

# (Default ping config)
HOST_TO_PING=google.com    # The host to monitor
PING_INTERVAL=5            # Check interval in seconds
PING_THRESHOLD=120         # Alert threshold in milliseconds
```

The program will:

1. Connect to Discord using your bot token
2. Start monitoring ping to the specified host
3. Send notifications when ping exceeds your threshold
4. Update the bot's RPC to reflect current ping conditions and more!

## 🔮 Future Goals

Planned features and improvements for upcoming releases:

- [X] ~~*More user friendly setup and startup*~~
  - **``v1.4.0.``**
- [X] ~~*Bot mentions discord user in high ping alert message*~~
  - **``v2.5.0.``**
- [ ] Bot edits message so it shows how long did it take for ping to settle
  - **``Planned to be implemented before v3.0.0.``**
- [ ] Better UI for startup and setup
  - **``Planned to be implemented after v3.0.0.``**
- [ ] Optimize code
  - **``Planned to be implemented in the near future.``**
- [ ] Create leaderboard which displays the highest ping recorded throughout specified period (make it somehow multi-user)
  - **``Planned for the distant future, pending feasibility.``**
- [ ] Docker container support
  - **``N/A``**
- [ ] Cross-platform compatibility (Linux, Windows)
  - **``N/A``**

Got an idea or feature request? Feel free to open an [issue](https://github.com/bebe-Kexe/ping-monitor-x-discord/issues)


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/bebe-Kexe/ping-monitor-x-discord/blob/main/LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 🔮 Future Goals
Planned features and improvements for upcoming releases:

- [x] More user friendly setup and startup
- [ ] Bot mentions discord user in high ping alert message
- [ ] Docker container support  
- [ ] Cross-platform compatibility (Linux, Windows)

Got an idea or feature request? Feel free to open an [issue](https://github.com/bebe-Kexe/ping-monitor-x-discord/issues)

---

Made with ❤️ by [Kexe](https://github.com/bebe-Kexe) while waiting for better ping.
