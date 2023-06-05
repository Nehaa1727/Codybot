from telethon import events
from .. import bot
from .. import openai_key 
import asyncio
import openai

openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern= "(?i)/ask"))
async def chatgpt(event):
  if event.sender_id == int(1314662073) :
    await event.reply("You are my Developer! You developed me very well")
  else:
    await event.reply("You are user ! Nice to meet you")
  
  
