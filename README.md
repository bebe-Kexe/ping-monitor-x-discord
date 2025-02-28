# Ping Monitor with Discord Notifications

A Python-based utility that monitors your network ping in real-time and sends alerts to Discord when latency exceeds a specified threshold.

![Discord Notification Example](https://media.discordapp.net/attachments/1019689698584690710/1344670229413892107/5f30XFiOJ5aa2uxWJtW1394hrwmwDT5JdPCbIEtaoid7NLOWZhv9wkWCCoAQMxrarmlceEtyhuGaRlDxtUmlsrC9wU8SfJ1V46Qmr6pnBHHZd6daThgEOUKT2luW1a864sir8am5sLhTuQ6hHyFEHgVEs6Hc2FoPD9gQdSaIN6TJb7ldTHxGCVM5rUNFD5.png?ex=67c1c13d&is=67c06fbd&hm=08a9a3b5bc9962838d28694033d5fb0153fb29b4270c43c826ce3584539fc3b5&=)

## 🌟 Features

- **Real-time ping monitoring** to a specified host (default: google.com)
- **Discord notifications** when ping exceeds the threshold
- **Custom status** on your Discord bot showing your current ping condition
- **Configurable thresholds** to match your needs
- **Robust error handling** to prevent crashes
- **User-friendly** setup and startup scripts with batch files

## 📋 Requirements

- Python 3.7+
- Discord bot token and permissions
- Internet connection 

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bebe-Kexe/ping-monitor-x-discord.git
   cd ping-monitor-discord
   ```
   - _Full release **WIP**_

2. Install dependencies:
   - Simply double-click ``setup.bat``





## 💻 Usage

Run the script with:

- Double-click ``start.bat``
   - If this is your first time running it, a ``.env_vars`` file will be created. Open it with a text editor and specify ``DISCORD_TOKEN``, ``CHANNEL_ID``, and ``USER_NAME`` (optional).
 

## ⚙️ Configuration

Edit the following variables in .env_vars to customize your experience:

```python
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

## 📊 How It Works

1. The script uses `ping3` library to measure network latency to a target host
2. When latency exceeds the threshold, a Discord webhook is triggered
3. A rich embed is sent to your specified Discord channel with ping information
4. The Discord bot status is updated to reflect the current situation
5. When ping returns to normal levels, the status is updated accordingly


## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 🙏 Acknowledgements

- [ping3](https://github.com/kyan001/ping3) for the ping implementation
- [discord.py](https://github.com/Rapptz/discord.py) for the Discord API wrapper

---

Made with ❤️ by [Kexe](https://github.com/bebe-Kexe)
