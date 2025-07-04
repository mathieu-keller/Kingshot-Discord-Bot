# Kingshot Discord Bot

## 🎮 What is this?
A comprehensive Discord bot for Kingshot alliance management, featuring gift code redemption, member tracking, event notifications, and more. This bot is specifically designed for [Kingshot](https://www.centurygames.com/games/kingshot/).

## 🖥️ Prerequisites

- **[Python 3.9 or later](https://www.python.org/downloads/) is required to run the bot**
- Can be run on Windows, Linux, Raspberry Pi, a Docker container, or even on your mobile phone
- System requirements are minimal (at least until captcha is added to the gift code site)
- No GPU required - all processing is CPU-based
- Stable internet connection required

## 🚀 Installation

> Detailed installation and hosting guides are available on our [Discord](https://discord.gg/HFnNnQWnbS). Come join the community!

**Before following the steps below, you should have already completed the bot setup on the Discord Application Portal.** If not, please first do the following Bot Creation steps.

### Bot Creation Process
1. Go to the [Discord Application Portal](https://discord.com/developers/applications)

2. Click **New Application**, name it, and click **Create**.
Add an App Icon and Description if you like.
This determines how your Bot will appear on your Discord server.

3. On the left, go to **Settings > OAuth2**, and under **OAuth2 URL Generator**, select:
* ✅ bot

4. A **Bot Permissions** window will open below, select:
* ✅ Administrator

Next to the Generated URL at the bottom of the page, click **Copy** and then paste the URL into your web browser.

5. Select your Discord server and follow the steps to add the bot to the server.

6. Go back to the **Discord Application Portal** and make sure your bot is selected.

7. Click on **Bot** on the left settings menu.

8. On the page that opens, under **Privileged Gateway Intents**, enable:

* ✅ Server Members Intent
* ✅ Message Content Intent
* ✅ Presence Intent

9. Click **Reset Token**, confirm, and copy the bot token.

10. Save this token in a text file named `bot_token.txt`. **Keep it safe!** You will also need it later on in the instructions.

### Bot Installation Steps

1. **Download the Bot files from Github, for example with [git](https://git-scm.com/downloads):**
   ```bash
   git clone https://github.com/justncodes/Kingshot-Discord-Bot.git
   cd Kingshot-Discord-Bot
   ```

2. **Install Bot Token:**
    Place the `bot_token.txt` file that you saved during the steps above into the Kingshot-Discord-Bot directory that your bot files are located in. If you don't, the bot will prompt you for the token during first start.
  
3. **Start the Bot:**
   Run the bot using Python from the command line. The bot will automatically install required dependencies when you first run it:
   ```bash
   python main.py
   ```

    * If you intend to run the bot headless (as a service), you can add the `--autoupdate` argument to skip the update prompt on restart:
  
   ```bash
   python main.py --autoupdate
   ```

4. **Initial Setup:**
   - Run `/settings` in Discord to configure yourself as the main administrator
   - Run `/settings` again to open the bot configuration menu
   - Use `/w [player-id]` for player lookup based on their ID

### Upgrading from previous versions

If you're using a previous version, **you only need to restart the bot** and accept the prompt asking you whether you want to update. The update should be seamless. If you prefer to skip the prompt, run the bot with the `--autoupdate` argument shown in the installation steps above.

## 🌟 Features

### 🏰 Alliance Management
- Add, edit, and manage multiple alliances
- Automatic member tracking and monitoring  
- Alliance-specific admin permissions
- Real-time member updates and notifications

### 🎁 Gift Code Operations
- **Manual Gift Code Management:** Add, view, and delete gift codes
- **Automatic Redemption:** Set up automatic gift code usage for alliances
- **Gift Code Channel Monitoring:** Monitor Discord channels for new gift codes
- **Bulk Redemption:** Redeem codes for entire alliances at once
- **Code Validation:** Automatic validation and cleanup of expired codes

### 👥 Member Operations
- Add and remove alliance members
- Bulk member operations (add multiple IDs at once)
- View member lists and statistics
- Transfer members between alliances
- Track member changes and history

### 🔧 Bot Operations
- Add and manage bot administrators
- Alliance-specific admin permissions
- Automatic update system
- Database backup and restore
- Comprehensive logging system

### 📊 Other Features
- **Notification System:** Event reminder system with flexible configuration and timing
- **ID Channel System:** Automatic member addition via ID channels
- **Backup System:** Encrypted database backups with personal encryption keys
- **Alliance History:** Track nickname and furnace level changes
- **Real-time Progress Tracking:** Live updates with color-coded status indicators

## 🔄 Auto-Update System

The bot includes an automatic update system:
- Checks for updates on startup
- Downloads and installs updates from GitHub
- Automatically backs up your database before updates
- Prompts for confirmation before applying updates

To run with automatic updates (for non-interactive environments):
```bash
python main.py --autoupdate
```

## 📜 Version History

### V1.1.0 (Current)
- Significant modification of `main.py`, migrating to a new and improved Github Release-based update system. No replacement of `main.py` is needed, just restart the bot running V1.0 and it will prompt to update.
- Integration of all the latest features and fixes from the [Whiteout Bot](https://github.com/whiteout-project/bot) as appropriate. Too many changes and enhancements to list here - see the patch notes section of the Whiteout Bot for details. All features up to 1.2.0 are integrated except Gift Code redemption changes.
- Cosmetic changes to emojis and terminology, removed old references to Whiteout-specific terms.

### V1.0 (Initial Port)
- Initial release designed for Kingshot
- All API endpoints optimized for Kingshot integration
- Independent update system
- Optimized rate limit wait times
- Enhanced event management features

## 🛠️ Getting Help

Need assistance with the bot?

**Join our community for support and updates: [WOSLand Discord](https://discord.gg/h8w6N6my4a)**

The community can help with:
- Installation and setup issues
- Configuration questions  
- Feature requests and suggestions
- General bot support and troubleshooting

## 🤝 Contributing

Contributions and improvements are welcome to help enhance the bot. Feel free to fork the bot, make your changes and submit a PR back to this repository! You can also open an Issue if you encounter problems.