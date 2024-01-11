import asyncio
import telegram
import os 
import glob

list_of_files = glob.glob('/var/www/html/data/images/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
# using telegram.Bot
async def sendphoto(chat, photo):
    await telegram.Bot('6800086011:AAGXLaW6COGmLuJKDuOx_d6bbMj5JUDj6KE').send_photo(chat_id=166566232, photo=open(latest_file, 'rb'))
async def sendmsg(chat, msg):
    await telegram.Bot('6800086011:AAGXLaW6COGmLuJKDuOx_d6bbMj5JUDj6KE').sendMessage(chat_id=166566232,text=msg)
def telegramSend():
    asyncio.run(sendmsg('<chat-id>', 'Nuova foto scattata!'))
    asyncio.run(sendphoto('<chat-id>', '<photo>'))
count = 1





try:
        while True:
                if (count == 1):
                        import mysql.connector
                                # Creating connection object
                        mydb = mysql.connector.connect(
                                host = "159.203.136.91",
                                user = "photoboot1",
                                password = "minimoto",
                                database = "photoboot",
                        )               
                        cursor = mydb.cursor(buffered=True)
                                # Show database
                        #cursor.execute("UPDATE crediti SET coin = coin -2  WHERE id = '1'")
                        cursor.execute("UPDATE crediti SET crediti = crediti -1  WHERE id = '1'")
                        cursor.execute("UPDATE crediti SET gettoni = gettoni -1  WHERE id = '1'")
                        mydb.commit()
                        mydb.close()  
                        count = 1 
                        telegramSend()
                          
                        exit ()                       
except KeyboardInterrupt:
        exit ()











 

