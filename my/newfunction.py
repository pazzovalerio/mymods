from config import *

import RPi.GPIO as GPIO
import time
#import Adafruit_GPIO.SPI as SPI

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

def upCoinMeno1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = coin -1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()  
    #exit ()

def upCoinPlus1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = coin +1  WHERE id = '1'")
    mydb.commit()
    #mydb.close()
    #exit ()        


def upCreditiPlus1():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET crediti = crediti +1  WHERE id = '1'")
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
