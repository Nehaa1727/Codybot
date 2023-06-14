from telethon import TelegramClient
import logging
import time 


openai_key ="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"
api_id ="15334693"
api_hash = "a70a6aee50a682f654b784b2e8bc19d7"
bot_token = "6215146547:AAG8MegA5hucMsbKRjFU9ZiN7cKBUkiONe0"
bot = TelegramClient("xcodybot",api_id, api_hash).start(bot_token=bot_token)
