# Kingshot Discord Bot

Kingshot Discord Bot that supports alliance management, event reminders and attendance tracking, gift code redemption, minister appointment planning and more. This bot is free, open source and self-hosted. This bot is specifically designed for [Kingshot](https://www.centurygames.com/games/kingshot/).

## 🖥️ Prerequisites

- **[Python 3.9 (64-bit) or later](https://www.python.org/downloads/) is required to run the bot**
- Can be run on Windows, Linux, Raspberry Pi, a Docker container, or even on your mobile phone
- System requirements are minimal (unless CAPTCHA is added to the gift code site)
- No GPU required - all processing is CPU-based
- Stable internet connection required

 - If you run your bot non-interactively, for example as a systemd service on Linux, you should run `--autoupdate` to prevent the bot from using the interactive update prompt.

- ⚠️ If you run your bot on Windows, there is a known issue with onnxruntime + an outdated Visual C++ library. To overcome this, install [the latest version of Visual C++](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) and then run `main.py` again.

## ☁️ Hosting Providers

**⚠️ This is a self-hosted bot!** That means you will need to run the bot somewhere. You could do this on your own PC if you like, but then it will stop running if you shut the PC down. Luckily there are some other hosting options available which you can find on [our Discord server](https://discord.gg/apYByj6K2m) under the `#host-setup` channel, many of which are free.

We have a list of known working VPS providers below that you could also check out. **Please note that the bot developers are not affiliated with any of these hosting providers (except ikketim) and we do not provide support if your hosting provider has issues.**

| Provider       | URL                                | Notes                                 |
|----------------|------------------------------------|---------------------------------------|
| ikketim        | https://panel.ikketim.nl/          | Free, recommended, and supported by one of our community MVPs. Contact ikketim on Discord to get set up with the hosting. |
| SillyDev       | https://sillydev.co.uk/            | Free tier. Earn credits through ads to maintain. |
| Bot-Hosting    | https://bot-hosting.net/           | Free tier. Requires earning coins though CAPTCHA / ads to maintain. |
| Lunes          | https://lunes.host/                | Free tier with barely enough capacity to run the latest version of the bot. Least recommended host out of the list here. |

If you are aware of any additional free providers that can host the bot, please do let us know.


## 🚀 Installation

> Detailed installation and hosting guides are available on our [Discord](https://discord.gg/apYByj6K2m). Come join the community!

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
    *   Run `/settings` for the bot in Discord for the first time to configure yourself as the global admin.
    *   Run `/settings` again afterwards to access the bot menu and configure it.

### Upgrading from previous versions

If you're using a previous version, **you only need to restart the bot** and accept the prompt asking you whether you want to update. The update should be seamless. If you prefer to skip the prompt, run the bot with the `--autoupdate` argument shown in the installation steps above.

## 🧹 Post-Installation

1.  **🏰 Set up your Alliance(s):**
    * Once you access the bot menu, you'll want to create one or more Alliance(s) via `Alliance Operations` -> `Add Alliance`.
    * `Control Interval` determines how often the bot will update names and furnace level changes. Once or twice a day should be sufficient.

2.  **👥 Add Members to your Alliance(s):**
    * Add members manually to the alliance(s) you created via `Member Operations` -> `Add Member`.
    * You can set up a channel where members can add themselves via `Other Features` -> `ID Channel` -> `Create Channel`.
    * Members must be added using their in-game ID, found on their in-game profile.
    * There are several ways to get members added to the bot:
      * Manually collect the IDs from in-game via your members' profiles.
      * Ask all members to post their IDs in your configured ID Channel.

3.  **🤖 Use the Bot as you like...**
  
    With your alliance(s) populated, you can make use of other features. Some examples follow...
    * Assign alliance-specific admins via `Bot Operations` -> `Add Admin`.
    * Configure the `Gift Code Operations` -> `Gift Code Settings` -> `Automatic Redemption` for your alliance(s) to redeem gift codes for all members as soon as they are added/obtained.
    * Set up alerts for your in-game events using `Other Features` -> `Notification System` -> `Set Time`.
    * Keep track of event attendance using the `Other Features` -> `Attendance System` functionality.
    * Organize SvS prep week minister positions using `Other Features` -> `Minister Scheduling`.
    
> If you encounter issues with the bot, you can open an issue on Github or [join our Discord](https://discord.gg/apYByj6K2m) for assistance. We are always happy to help!

## 🚩 Optional Flags
Numerous flags are available that can be used to adjust how the bot runs. These must always added at the end of the startup command, separated by a space, eg. `python main.py --autoupdate`.

| Flag | Purpose |
|-------------|---------------------------------|
| `--autoupdate` | Automatically updates the bot on reboot if an update is found. Useful for headless installs. Used automatically if a container environment is detected.
| `--beta` | Pulls the latest code from the repository on startup (instead of checking for new releases). **This runs unstable code:** Use at your own risk!
| `--no-update` | Skips the bot's update check, even in container/CI environment. Mutually exclusive with `--autoupdate` and overrides it.
| `--repair` | Attempt to repair the installation by forcing an update to fix any missing files. Works with `--beta` as well.

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

### V1.1.1 (Current)

### V1.1.0
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

**Join our community for support and updates: [WOSLand Discord](https://discord.gg/apYByj6K2m)**

The community can help with:
- Installation and setup issues
- Configuration questions  
- Feature requests and suggestions
- General bot support and troubleshooting

## 🤝 Contributing

Contributions and improvements are welcome to help enhance the bot. Feel free to fork the bot, make your changes and submit a PR back to this repository! You can also open an Issue if you encounter problems.