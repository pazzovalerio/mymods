import sys
import glob
import os

sys.path.insert(0, "/home/pi/.local/lib/python3.9/site-packages/telegram")

import telegram
import asyncio

#bot = telegram.Bot(token='6800086011:AAGXLaW6COGmLuJKDuOx_d6bbMj5JUDj6KE')
#channel_id = '166566232'

list_of_files = glob.glob('/var/www/html/data/images/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)


#import asyncio
#import telegram

# using telegram.Bot
async def sendphoto(chat, photo):
    await telegram.Bot('6800086011:AAGXLaW6COGmLuJKDuOx_d6bbMj5JUDj6KE').send_photo(chat_id=166566232, photo=open(latest_file, 'rb'))

async def sendmsg(chat, msg):
    await telegram.Bot('6800086011:AAGXLaW6COGmLuJKDuOx_d6bbMj5JUDj6KE').sendMessage(chat_id=166566232,text=msg)

asyncio.run(sendmsg('<chat-id>', 'Nuova foto scattata!'))
asyncio.run(sendphoto('<chat-id>', '<photo>'))


