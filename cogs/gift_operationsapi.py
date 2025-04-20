import os
import json
import aiohttp
import asyncio
import sqlite3
import re
from datetime import datetime
import traceback
import discord
import ssl

class GiftCodeAPI:
    def __init__(self, bot):
        self.bot = bot
        self.api_url = "https://wosland.com/apidc/giftapi/giftcode_api.php"
        self.api_key = "serioyun_gift_api_key_2024"
        self.check_interval = 300
        
        if hasattr(bot, 'conn'):
            self.conn = bot.conn
            self.cursor = self.conn.cursor()
        else:
            self.conn = sqlite3.connect('db/giftcode.sqlite')
            self.cursor = self.conn.cursor()
            
        self.settings_conn = sqlite3.connect('db/settings.sqlite')
        self.settings_cursor = self.settings_conn.cursor()
        
        self.users_conn = sqlite3.connect('db/users.sqlite')
        self.users_cursor = self.users_conn.cursor()
        
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
        
        # asyncio.create_task(self.start_api_check())

    async def start_api_check(self):
        try:
            await asyncio.sleep(60)
            await self.sync_with_api()
            
            while True:
                await asyncio.sleep(self.check_interval)
                await self.sync_with_api()
        except Exception as e:
            traceback.print_exc()

    def __del__(self):
        try:
            self.conn.close()
            self.settings_conn.close()
            self.users_conn.close()
        except:
            pass
    
    # Original functionality pulling from Relo's API removed.
    # The functions now pretend to have run successfully.
    async def sync_with_api(self):
        return True
            
    async def add_giftcode(self, giftcode: str) -> bool:
        return True
            
    async def remove_giftcode(self, giftcode: str, from_validation: bool = False) -> bool:
        return True
            
    async def check_giftcode(self, giftcode: str) -> bool:
        return True

    async def validate_and_clean_giftcode_file(self):
        try:
            self.cursor.execute("SELECT giftcode FROM gift_codes")
            codes = self.cursor.fetchall()
            
            if not codes:
                return
                    
            for code_row in codes:
                code = code_row[0]
                status = await self.bot.get_cog('GiftOperations').claim_giftcode_rewards_wos("27370737", code)
                
                if status in ["TIME_ERROR", "CDK_NOT_FOUND", "USAGE_LIMIT"]:
                    await self.remove_giftcode(code, from_validation=True)
                    
                await asyncio.sleep(1)
                    
        except Exception as e:
            traceback.print_exc() 
