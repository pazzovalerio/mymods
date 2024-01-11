from function2 import *
from config2 import *
from threading import Thread
from time import sleep
import time 
import RPi.GPIO as GPIO

up0()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 1
inseriti = 0




#lcdProcessBar()
lcdReadAsinc = Thread(target=lcdReadDb)
lcdReadAsinc.start()



#telegramSendAsinc = Thread(target=telegramSend)
#telegramSendAsinc.start()





print("\n  SCRIPT AVVIATO\n")

try:
        while True:
                if (count == 1):
                        print("\n\n   ###------ INSERIRE MONETE ------### " "\n")
                        GPIO.wait_for_edge(17, GPIO.FALLING)
                        inseriti += 1
                        print("Inseriti " +str(inseriti)+"/2")
                        
			#call(["aplay", "/home/photoboot/my/tts/inseriti-un-euro.wav"])
                        if (inseriti == 1):
                                inseritiUnEuro()
                                upCoinPlus1()
                        if (inseriti >= 2):
                                upCoinMeno1()
                                upCreditiPlus1()
                                inseriti = 0
                                creditoRaggiunto()
                                print("\n\n\n###########################################################")  
                                print("\n#####   CREDITO RAGGIUNTO! ADESSO SCATTA UNA  FOTO   #####" "\n")
                                print("###########################################################\n\n\n") 
                                time.sleep(3)
                                #break

                        
                                

except KeyboardInterrupt:
        GPIO.cleanup()












 

