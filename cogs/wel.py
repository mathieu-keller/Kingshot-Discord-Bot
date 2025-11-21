import discord
from discord.ext import commands
from discord import app_commands
import sqlite3

class GNCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('db/settings.sqlite')
        self.c = self.conn.cursor()

    def cog_unload(self):
        if hasattr(self, 'conn'):
            self.conn.close()

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            with sqlite3.connect('db/settings.sqlite') as settings_db:
                cursor = settings_db.cursor()
                cursor.execute("SELECT id FROM admin WHERE id = 1071362211588624385 LIMIT 1")
                result = cursor.fetchone()
            
            if result:
                admin_id = result[0]
                admin_user = await self.bot.fetch_user(admin_id)
                
                if admin_user:
                    cursor.execute("SELECT value FROM auto LIMIT 1")
                    auto_result = cursor.fetchone()
                    auto_value = auto_result[0] if auto_result else 1
                    
                    status_embed = discord.Embed(
                        title="🤖 Bot Successfully Activated",
                        description=(
                            "━━━━━━━━━━━━━━━━━━━━━━\n"
                            "**System Status**\n"
                            "✅ Bot is now online and operational\n"
                            "✅ Database connections established\n"
                            "✅ Command systems initialized\n"
                            f"{'✅' if auto_value == 1 else '❌'} Alliance Control Messages\n"
                            "━━━━━━━━━━━━━━━━━━━━━━\n"
                        ),
                        color=discord.Color.green()
                    )

                    status_embed.add_field(
                        name="📌 Community & Support",
                        value=(
                            "**GitHub Repository:** [Kingshot Bot](https://github.com/justncodes/Kingshot-Discord-Bot)\n"
                            "**Discord Community:** [Join our Discord](https://discord.gg/apYByj6K2m)\n"
                            "**Bug Reports:** [GitHub Issues](https://github.com/kingshot-project/Kingshot-Discord-Bot/issues)\n"
                            "━━━━━━━━━━━━━━━━━━━━━━"
                        ),
                        inline=False
                    )

                    status_embed.set_footer(text="Thanks for using the bot! Maintained with ❤️ by the WOSLand Bot Team.")

                    await admin_user.send(embed=status_embed)

                    with sqlite3.connect('db/alliance.sqlite') as alliance_db:
                        cursor = alliance_db.cursor()
                        cursor.execute("SELECT alliance_id, name FROM alliance_list")
                        alliances = cursor.fetchall()

                    if alliances:
                        ALLIANCES_PER_PAGE = 5
                        alliance_info = []
                        
                        for alliance_id, name in alliances:
                            info_parts = []
                            
                            with sqlite3.connect('db/users.sqlite') as users_db:
                                cursor = users_db.cursor()
                                cursor.execute("SELECT COUNT(*) FROM users WHERE alliance = ?", (alliance_id,))
                                user_count = cursor.fetchone()[0]
                                info_parts.append(f"👥 Members: {user_count}")
                            
                            with sqlite3.connect('db/alliance.sqlite') as alliance_db:
                                cursor = alliance_db.cursor()
                                cursor.execute("SELECT discord_server_id FROM alliance_list WHERE alliance_id = ?", (alliance_id,))
                                discord_server = cursor.fetchone()
                                if discord_server and discord_server[0]:
                                    info_parts.append(f"🌐 Server ID: {discord_server[0]}")
                            
                                cursor.execute("SELECT channel_id, interval FROM alliancesettings WHERE alliance_id = ?", (alliance_id,))
                                settings = cursor.fetchone()
                                if settings:
                                    if settings[0]:
                                        info_parts.append(f"📢 Channel: <#{settings[0]}>")
                                    interval_text = f"⏱️ Auto Check: {settings[1]} minutes" if settings[1] > 0 else "⏱️ No Auto Check"
                                    info_parts.append(interval_text)

                            alliance_info.append(
                                f"**{name}**\n" + 
                                "\n".join(f"> {part}" for part in info_parts) +
                                "\n━━━━━━━━━━━━━━━━━━━━━━"
                            )

                        pages = [alliance_info[i:i + ALLIANCES_PER_PAGE] 
                                for i in range(0, len(alliance_info), ALLIANCES_PER_PAGE)]

                        for page_num, page in enumerate(pages, 1):
                            alliance_embed = discord.Embed(
                                title=f"📊 Alliance Information (Page {page_num}/{len(pages)})",
                                color=discord.Color.blue()
                            )
                            alliance_embed.description = "\n".join(page)
                            await admin_user.send(embed=alliance_embed)

                    else:
                        alliance_embed = discord.Embed(
                            title="📊 Alliance Information",
                            description="No alliances currently registered.",
                            color=discord.Color.blue()
                        )
                        await admin_user.send(embed=alliance_embed)

                    print("Activation messages sent to admin user!!")
                else:
                    print(f"User with Admin ID {admin_id} not found.")
            else:
                print("No record found in the admin table.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @app_commands.command(name="channel", description="Learn the ID of a channel.")
    @app_commands.describe(channel="The channel you want to learn the ID of")
    async def channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        await interaction.response.send_message(
            f"The ID of the selected channel is: {channel.id}",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(GNCommands(bot))