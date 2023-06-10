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
  await asyncio.sleep(3)
  await a.edit("Here is the list of some famous web series and k-dramas...Enjoy🎉")
  await event.reply("""**Web Series**\n1. Money Heist\n2. Stranger Things\n3. Wednesday\n4. You\n5. Lucifer\n6. Never Have I Ever\n7. Kota Factory\n8. College Romance \n10. The Vampire Diaries\n11. Game of thrones\n12. Dark\n13. Panchayat \n14. Crash Course\n15. Sex Education
  \n\n**K-drama**\n1. All of us are dead\n2. Squid Game\n3. Business Proposal\n4. Happiness\n5. True Beauty\n6. What's Wrong With Secretary Kim\n7. It's Okay To Not Be Okay\n8. The Heirs\n9. Goblin: The Lonely And Great God\n10. Vincenzo\n11. School 2017\n12. Twenty Five Twenty One\n13. Crash Landing On You\n14. Nevertheless\n15. The Glory""")
  
  

@bot.on(events.NewMessage(incoming = True, pattern = "/eval"))
async def start(event):
  await event.reply("Hello! This is Eval Command")
  
 

@bot.on(events.NewMessage(incoming = True, pattern = "/help"))
async def start(event):
  await event.reply("""Hello Sir/Ma'am😊 I hope you are good and having a great day. I am Cody Bot developed by Neha Mundhra. Here are my following command :- \n\n1. /yta + 'link of any YouTube video' = It can help you to download the audio from YouTube Platform.\n\n2. /ytv + 'link of any YouTube video' = It can help you to download the video from YouTube Platform.\n\n3. /tr + 'language code' + 'any sentence as well as emoji' = It can translate the sentence into the language code you have entered.\n\n4. /get = It will provide you the list of some web series and K-dramas """
  )
  