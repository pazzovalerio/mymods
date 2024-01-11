from config2 import *
from subprocess import call
import drivers
from time import sleep
import os
import psutil
import redis
import sys
import glob
import telegram
import asyncio


#list_of_files = glob.glob('/var/www/html/data/images/*') # * means all if need specific format then *.csv
#latest_file = max(list_of_files, key=os.path.getctime)




r = redis.StrictRedis(decode_responses=True)

display = drivers.Lcd()



#import RPi.GPIO as GPIO
#import time

def upCoinMeno1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = coin -1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()

def upCreditiPlus1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET crediti = crediti +1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()

def upCoinPlus1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = coin +1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()
    #exit ()     


def inseritiUnEuro():
    call(["aplay", "/home/photoboot/my/tts/inseriti-un-euro.wav"])

def avvioInCorso():
    call(["aplay", "/home/photoboot/my/tts/avvio-in-corso.wav"])

def creditoRaggiunto():
    call(["aplay", "/home/photoboot/my/tts/credito-raggiunto.wav"])


def lcdReadDb():
	display.lcd_clear()
	#print("Press CTRL + C to stop this script!")

	def long_string(display, text='', num_line=1, num_cols=16):
		""" 
		Parameters: (driver, string to print, number of line to print, number of columns of your display)
		Return: This function send to display your scrolling string.
		"""
		if len(text) > num_cols:
			display.lcd_display_string(text[:num_cols], num_line)
			sleep(1)
			for i in range(len(text) - num_cols + 1):
				text_to_print = text[i:i+num_cols]
				display.lcd_display_string(text_to_print, num_line)
				sleep(0.3)
			sleep(1)
		else:
			display.lcd_display_string(text, num_line)


	# Example of short string
	long_string(display , "Photoboot", 1)
	long_string(display ,"By Valex | Per assistenza ", 2)
	sleep(3)
	display.lcd_clear()


	display.lcd_display_string("Email :", 1)
	long_string(display ,"coccia.valerio@gmail.com ", 2)
	sleep(3)
	display.lcd_clear()


	display.lcd_display_string("Telefono : ", 1)
	display.lcd_display_string("3451238135", 2)
	


	while True:
		total_memory, used_memory, free_memory = map(
    		int, os.popen('free -t -m').readlines()[-1].split()[1:])
		cpu = psutil.cpu_percent(4)
		ram = round((used_memory/total_memory) * 100, 2)
		display.lcd_clear()
		xxcoin=int(r.get("coin"))
		xxid=int(r.get("id"))
		xxcrediti=int(r.get("crediti"))
		xxgettoni=int(r.get("gettoni"))
		xxnome=r.get("nome")

		# An example of infinite scrolling text
		display.lcd_display_string("CPU: " + str(cpu) + "%", 1)
		display.lcd_display_string("RAM: " + str(ram) + "%", 2)
		sleep(2)
		display.lcd_clear()


		display.lcd_display_string("MEMORIA: 50% ", 1)
		display.lcd_display_string("WIFI   : 50%", 2)
		sleep(2)
		display.lcd_clear()

		display.lcd_display_string(str(xxnome),1)
		display.lcd_display_string("ID : " + str(xxid) ,2)
		sleep(3)
		display.lcd_clear()


		display.lcd_display_string("COIN   : " + str(xxcoin),1)
		display.lcd_display_string("CREDITI: " + str(xxcrediti),2)
		sleep(3)
		display.lcd_clear()

		display.lcd_display_string("GETTONI : " + str(xxgettoni),1)
		
		

# using telegram.Bot
async def sendphoto(chat, photo):
    await telegram.Bot('6800086011:AAGXLaW6COGmLuJKDuOx_d6bbMj5JUDj6KE').send_photo(chat_id=166566232, photo=open(latest_file, 'rb'))
async def sendmsg(chat, msg):
    await telegram.Bot('6800086011:AAGXLaW6COGmLuJKDuOx_d6bbMj5JUDj6KE').sendMessage(chat_id=166566232,text=msg)
def telegramSend():
    asyncio.run(sendmsg('<chat-id>', 'Nuova foto scattata!'))
    asyncio.run(sendphoto('<chat-id>', '<photo>'))














def up0():
    cursor = mydb.cursor(buffered=True)
    result = []
    cursor.execute("UPDATE crediti SET coin = 0  WHERE id = '1'")
    cursor.execute("UPDATE crediti SET crediti = 0  WHERE id = '1'")
    mydb.commit()
    #mydb.close()
    #exit ()

def upCrediti1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET crediti = 1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()      

def upCoin0():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = 0  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()   

def upCoinMeno2():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = coin -2  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()      



  






def upGettoniMeno1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET gettoni = gettoni -1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit () 



def updateDatabaseLocale():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = 1  WHERE id = '1'")
   # mydb.commit()
    mydb.close()  
    exit () 





def Up(idr):
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET crediti = crediti +1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()


def readRem(idr):
    global rows
    global id
    global coin
    global crediti
    global nome 
    global gettoni 
    cursor = mydb.cursor(buffered=True)
    try:  
    #Reading the Employee data      
        cursor.execute("select * from crediti")  
      #fetching the rows from the cursor object  
        rows = cursor.fetchall()
        user = rows[idr -1] 
        id = user[0]
        coin = user[1]
        crediti = user[2]
        nome = user[3]
        gettoni = user[4]

    except:  
        mydb.rollback()
    finally:
        mydb.commit()
        mydb.close()
        #mydb.commit() 
        #exit ()
    return(id,coin,crediti,nome,gettoni)
    #exit ()

def isOnline():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET status = 1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()    
 

def isOffline():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET status = 0  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()   

def check():
    while not internet_on():
        pass
    print ("internet connection is on")

import urllib.request as urllib2
def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False
