"""Check Your Internet Speed"""
from telethon import TelegramClient
from telethon import events
from .. import bot 
import os 


@bot.on(events.NewMessage(incoming=True, pattern="/speedtest"))
async def speedtest(event):
    chat = await event.get_chat()
    message = await event.reply("Checking Your Internet Speed...Please Wait😊")

  #Command execution and retrieve the output as a string  
    response = os.popen('speedtest-cli --simple').read()
    a = response.split('\n')

 
    download_speed = None
    upload_speed = None 
    #None indicates that the values are not known yet
    #The code iterates over each line in the 'lines' list which checks each line to  see if it contains the keywords 'Download' or 'Upload'
    for a in a:
        if 'Download' in a:
            download_speed = a.split(':')[1].strip()
        elif 'Upload' in a:
            upload_speed = a.split(':')[1].strip()
    #If a line contain the keyword then it is split at colon, resulting in a list of two elements i.e. the text before(ignorable) and after colon . 
    #The 'a.split(':')[1] fetch second element, which represent speed value.
    #strip() method remove any leading or trailing whitespace.


    if download_speed != None and upload_speed != None:      response_message = f"**Download speed:** {download_speed}\n**Upload speed:** {upload_speed}"
    #Speed values assigned
    else:
        response_message = "Failed to fetch the internet speed."

   
    await message.edit(response_message)


