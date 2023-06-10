from .. import bot,openai_key
from telethon import events
import asyncio
import openai 

openai.my_api_key = openai_key

@bot.on(events.NewMessage(incoming = True, pattern = "/start"))
async def start(event):
  await event.reply("Hello! This is Cody Bot \n\nType **/help** for the further information")
  

@bot.on(events.NewMessage(incoming = True, pattern = "/get"))
async def start(event):
  a = await event.reply("Hello! This is Get Command")
  await asyncio.sleep(1)
  await a.edit("This is edited message")
  

@bot.on(events.NewMessage(incoming = True, pattern = "/eval"))
async def start(event):
  await event.reply("Hello! This is Eval Command")
  
 

@bot.on(events.NewMessage(incoming = True, pattern = "/help"))
async def start(event):
  await event.reply("""Hello Sir/Ma'am😊 I hope you are good. I am Cody Bot developed by Neha Mundhra. Here are my following command :- \n\n1. /yta + 'link of any YouTube video' = It can help you to download the audio from YouTube Platform.\n\n2. /ytv + 'link of any YouTube video' = It can help you to download the video from YouTube Platform.\n\n3. /tr + 'language code' + 'any sentence as well as emoji' = It can translate the sentence into the language code you have entered. """
  )
  