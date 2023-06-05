from telethon import TelegramClient
import logging
import time 


openai_key ="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"
api_id = "15334693"
api_hash = "a70a6aee50a682f654b784b2e8bc19d7"
bot_token = "6100324704:AAHP9mADSNpQV4Ssi5EdA1OoKascwHr7rdo"

bot = TelegramClient("codybot",api_id, api_hash).start(bot_token=bot_token)