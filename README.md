# Ping Monitor with Discord Notifications

A Python-based utility that monitors your network ping in real-time and sends alerts to Discord when latency exceeds a specified threshold.


<p align="center">
  <img src="https://media.discordapp.net/attachments/1019689698584690710/1344670229413892107/5f30XFiOJ5aa2uxWJtW1394hrwmwDT5JdPCbIEtaoid7NLOWZhv9wkWCCoAQMxrarmlceEtyhuGaRlDxtUmlsrC9wU8SfJ1V46Qmr6pnBHHZd6daThgEOUKT2luW1a864sir8am5sLhTuQ6hHyFEHgVEs6Hc2FoPD9gQdSaIN6TJb7ldTHxGCVM5rUNFD5.png?ex=67c1c13d&is=67c06fbd&hm=08a9a3b5bc9962838d28694033d5fb0153fb29b4270c43c826ce3584539fc3b5&=" alt="Discord Notification Example">
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

- **Real-time ping monitoring** to a specified host (default: google.com)
- **Discord notifications** when ping exceeds the threshold
- **Custom status** on your Discord bot showing your current ping condition
- **Configurable thresholds** to match your needs
- **Robust error handling** to prevent crashes
- **User-friendly** setup and startup scripts with batch files

## 📋 Requirements

- Python 3.11+ (recommended)
- Discord bot token and permissions
- Internet connection 



## 🚀 Installation

1. Download [**LATEST RELEASE**](https://github.com/bebe-Kexe/ping-monitor-x-discord/releases) zip (always called after the version)
   - Unzip it into your desired directory

3. Install dependencies:
   - Open the ``ping-monitor-x-discord`` folder
   - Simply double-click ``setup.bat``

## 💻 Usage

Run the script with:

- Double-click ``start.bat``
   - If this is your first time running it, a ``.env_vars`` file will be created. Open it with a text editor and specify ``DISCORD_TOKEN``, ``CHANNEL_ID``, and ``USER_NAME`` (optional).

## ⚙️ Configuration

Edit the following variables in .env_vars to customize your experience:

```.env_vars
DISCORD_TOKEN=xxx.yyy.zzz  # Replace with bot token
CHANNEL_ID=1234567890      # Replace with channel ID
USER_NAME=@xxxxxx          # Replace with your username (optional)
HOST_TO_PING=google.com  # The host to monitor
PING_INTERVAL=5            # Check interval in seconds
PING_THRESHOLD=120         # Alert threshold in milliseconds (ms)
```

The program will:
1. Connect to Discord using your bot token
2. Start monitoring ping to the specified host
3. Send notifications when ping exceeds your threshold
4. Update the bot's status to reflect current ping conditions 



## 🔮 Future Goals
Planned features and improvements for upcoming releases:

- [x] More user friendly setup and startup
- [x] Bot mentions discord user in high ping alert message
- [ ] Bot counts how long did it took for ping to settle 
- [ ] **Split Bulk Delete and Individual Delete**: Implement a two-phase message deletion system that:
      - First identifies messages newer than 14 days and deletes them in bulk (fast)
      - Then handles older messages individually with proper rate limiting (slower)
      - Provides real-time progress feedback to users during deletion
      - Allows cancelling long-running deletion operations
- [ ] Docker container support  
- [ ] Cross-platform compatibility (Linux, Windows)
- [ ] Bot sends high ping message to multiple channels

Got an idea or feature request? Feel free to open an [issue](https://github.com/bebe-Kexe/ping-monitor-x-discord/issues)



## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/bebe-Kexe/ping-monitor-x-discord/blob/main/LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 🙏 Acknowledgements

- [ping3](https://github.com/kyan001/ping3) for the ping implementation
- [discord.py](https://github.com/Rapptz/discord.py) for the Discord API wrapper

---

Made with ❤️ by [Kexe](https://github.com/bebe-Kexe) while waiting for better ping.
