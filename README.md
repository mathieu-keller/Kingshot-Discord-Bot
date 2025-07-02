# Kingshot Discord Bot
Discord Bot for [Kingshot](https://www.centurygames.com/games/kingshot/). Features include automated gift code redemption, notifications for events, alliance member tracking, Player ID input and more.

It is essentially a reskin of the Whiteout Survival Bot that [Relo](https://github.com/Reloisback) made.

Enjoy, and if it doesn't work, blame the server hamsters!

### 🎁 Gift Code System
- Introduced new Gift Code API system
- Shared gift code database for easier management
- Automatic expired code cleanup
- Alliance auto-gift code usage feature
  - Automatically detects and applies codes for all members
  - Customizable periodic alliance checks

### 📢 Notification System
- Unlimited custom notifications
- Flexible timing configuration
- Multiple notification intervals
- Example scenario:
  ```
  Event time: 18:00 UTC
  Notifications at:
  - 17:40 (20 minutes before)
  - 17:50 (10 minutes before)
  - 17:55 (5 minutes before)
  - 18:00 (Event start)
  ```
- Web interface for notification management
  - Visit: [wosland.com/notification](https://wosland.com/notification)

### 💾 Backup System
- Automatic database backup
- Secure encrypted backups (.zip format)
- Personal encryption key system
- Private backup link generation
- Enhanced data privacy
  - Only member IDs are stored
  - Encrypted access

### 🆔 ID Channel System
- Automatic alliance member addition
- Discord channel integration
- Duplicate entry prevention
- Comprehensive logging system

### ⚙️ Additional Features
- Alliance Control Messages toggle in Bot Operations menu
- Customizable progress notifications
- Enhanced user experience

### 🌟 Support & Community
Join our Discord community for:
- Direct support
- Feature requests
- Updates and announcements
- [Join Discord Server](https://discord.gg/h8w6N6my4a)

### 🔄 Changes for Kingshot
- All redemption requests now point to kingshot-giftcode.centurygame.com
- Updated the old secret key to the new super-secret key (thanks Bahraini)
- Change auto-update references to use this Github repository instead (avoid Whiteout Bot changes overriding Kingshot changes)
- Removed the fallback to wosland.com autoupdateinfo if Github cannot be reached (see above)
- Reset the version numbering in autoupdateinfo to V1.0
- Reduced wait time after API "rate limit" hit to 30s by default
- Changed ID used to verify gift codes to a KS Player ID 27370737
- Removed the gift code retrieval from Relo's external gift code API

### 🛠️ Fixes for Kingshot
- Added the fix from my [PR #26](https://github.com/Reloisback/Whiteout-Survival-Discord-Bot/pull/26) to view/edit/delete with 25+ events

### 📝 Upcoming Features
- Implementing fixed days scheduling for events (eg. every Tuesday, Thursday, Sunday)
- Pulling in additional fixes from the original bot PRs

## Main Menu Buttons

### 🏰 Alliance Operations
- Add, remove and edit alliances
- Seeing Existing Alliances

### 👥 Member Operations
- Add, delete and view alliance members
- Member transfer from Alliance to Alliance

### ⚙️ Bot Operations
- Adding, deleting and viewing admins
- Alliance-specific admin authorization and deletion
- Transferring old V3 and V2 database information 
- Checking Bot Updates
- Log System (The log channel you select to see the members added and deleted by administrators)
### 📜 Alliance History Menu
- View nickname and furnace level history of any member or alliance
### 🆘 Support Operations
- Help and developer information
- Direct contact options

### 🔧 Other Features
- Opens additional features menu
- Reserved for future updates
# Button Descriptions
## 🏰 Alliance Operations Menu

### ➕ Add Alliance
- Pressing this Button prompts you for 3 pieces of information
- Alliance name and Interval time (Interval time is how many minutes it will check automatically, if you type 0, there will be no automatic check)
- It then prompts you to select a channel and shows both the automatically redeemed gift code information and the names and oven levels that change under automatic alliance control.

### 🗑️ Delete Alliance
- Deletes all information and members of your selected alliance

### ✏️ Edit Alliance
- Allows you to change the name, control time or control channel of the alliance you added

### 👀 View Alliances
- Shows your alliance lists, how many members it has and how often it is checked

## 👥 Member Operations Menu

### ➕ Add Members
- Used to add members to your alliance
- When you press the button, it asks you for 2 pieces of information:
  - First it asks which alliance you want to add members to
  - Then you will be asked to enter the IDs of the players in the window that appears, (id1,id2,id3 you can add in bulk)
  - If members are added, you will be able to see them moment by moment
- It records the details of the added members here, i.e. their logs: `log/add_memberlog.txt`
### ➖ Remove Member
- Press this and it asks you to choose an alliance
- Then it shows the members of the alliance, you can either delete them all or select 1 member and delete it
### 📋 View Members
- When you press it, it asks you to choose an alliance,
- Then shows the members of the alliance

## 🤖 Bot Operations Menu
 > 90% of the buttons in this menu can only be used by the owner of the bot

### ➕ Add Admin

- This feature adds admin to your bot. 
- After pressing it, it asks you to tag the admin
    - The administrators you add cannot access all settings.
    - They can only see and manage alliances in the discord they are in.
    - They can also see specially authorized alliances

### ➖ Remove Admin

- Press this and it will show you the list of attached admins
- When you select the administrator, it shows you the details and deletes the administrator if you confirm

### 👥 View Administrators

- Shows your admin list and displays the current authorizations of the admins

### 🔗 Assign Alliance to Admin

- Allows you to assign a custom alliance management to the admins you add
- This is done in different discord server so that the admins you want can see the other alliances

### ➖ Delete Admin Permissions

- This feature allows you to delete the alliance management that you have specifically assigned to the admins

### 🔄 Transfer Old Database

- For those who use V2 or V3, it is made to transfer the old database to the V4 database
- If you put the V2 or V3 database in the file location where main.py is located and then press this button and select the correct version, your members, your members' changes gift codes will be transferred automatically

### 🔄 Check for Updates

- If you check if there is a new version of the bot
- It will tell you what has changed, if anything

### 📋 Log System

- This button allows you to select the admin log management channel
- It will tell you to choose an alliance, and after choosing an alliance, it will tell you to choose the discord channel.
- Shows the actions of the administrators who add or delete members on that channel

## 🎁 Gift Code Operations

### 🎫 Create Gift Code

- This button allows you to add gift code manually

### 📋 List Gift Codes

- This button lists the attached gift codes

### ❌ Delete Gift Code

- This button allows you to delete gift code

### 📢 Gift Code Channel

- This button checks gift code
- It asks you to choose an alliance and then asks you to choose a discord channel
- Checks the giftcode written by each user in this discord channel
- If it is a valid giftcode, it adds it to the database
- If the alliance's automatic gift code usage option is active, it will be used for the whole alliance
- You can add the channel of your choice by following the messages of the gift code channel from the WOS discord
- Automatically detects gift codes here

### 🗑️ Delete Gift Channel

- Deletes the channel that controls the written gift codes

### ⚙️ Auto Gift Settings

- When you press this button it asks you to choose an alliance
- If the alliance is approved and the alliance has a Gift Code Channel
- It always uses the successful gift codes it captures there for the approved alliance

### 🎯 Use Gift Code for Alliance

- Prompts you to choose an alliance and a gift code, then redeems the gift code for everyone in that alliance

## 📝 Alliance History Menu

### 🔥 Furnace Changes

- Pressing this button opens the alliance list
- After selecting an alliance, the alliance member list will appear, displaying the history of Furnace Changes of the selected member
- Or you can enter a number between 1 and 24 hours to see all alliance members who made changes within this interval

### 📝 Nickname Changes

- Pressing this button opens the alliance list
- After selecting an alliance, the alliance member list will appear, displaying the history of Nickname Changes of the selected member
- Or you can enter a number between 1 and 24 hours to see all alliance members who made changes within this interval
