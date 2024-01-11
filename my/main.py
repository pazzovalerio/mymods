from newfunction import *
from config import *
from threading import Thread
import time 

import drivers
from time import sleep
from newfunction import *
from config import *
import redis

from subprocess import call



r = redis.Redis()
display = drivers.Lcd()








#update dal database tramite id sudo 
#macLocal = readLocal(id_macchina)
#macRem = readRem(id_macchina)

#print("\n\n\nCoin remoti  = " + str(mac[1]) +"    ------ INSERIRE MONETE ------ " "\n\n")

#print("\n\n\nCREDITIiiiiiii remoti  = " + str(mac[2]) +"    ------ INSERIRE MONETE ------ " "\n\n")

#updateOled(1) 
#         
#print("remoto  | " + str(readRem(id_macchina)))


#print('ID LOCALI | ' + str(macLocal[id]))
#print('COIN LOCALI | ' + str(macLocal[coin]))
#print('CREDITI LOCALI | ' + str(macLocal[crediti]))

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
count = 1
counter = 0
#crediti = 0
inseriti = 0
print("\n\nSCRIPT AVVIATO   "    "   ------ INSERIRE MONETE ------ " "\n\n")

try:
        while True:
                if (count == 1):
                        GPIO.wait_for_edge(17, GPIO.FALLING)
                        counter += 1
                        print("Inseriti " +str(counter)+"/2")
			call(["aplay", "/home/photoboot/my/tts/inseriti-un-euro.wav"])
			upCoinPlus1()
                        if (counter == 1):
                                inseriti = 1
                                t = Thread(target=upCoinPlus1)
                                t.start()
                                #upCoinPlus1()
                        if (counter >= 2):
                                time.sleep(3)
                                #upCoinPlus1()
                                upCoinMeno1()
                                upCreditiPlus1()
                                counter = 0  
                                print("\nCREDITO RAGGIUNTO! ADESSO SCATTA UNA  FOTO")
                                break

                        
                                

except KeyboardInterrupt:
        GPIO.cleanup()












 

