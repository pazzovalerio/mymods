from newfunction import *
from config import *
from threading import Thread
import time 

import drivers
from time import sleep
from newfunction import *
from config import *
import redis
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

	display.lcd_clear()
	print("Press CTRL + C to stop this script!")

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
				sleep(0.1)
			sleep(1)
		else:
			display.lcd_display_string(text, num_line)


	# Example of short string
	long_string(display , "Avvio in corso", 1)
	sleep(1)

	# Example of long string
	display.lcd_display_string("PhotoBoot By Valex     |  Per assistenza ", 2)
	display.lcd_clear()
	display.lcd_display_string("Email :", 1)
	display.lcd_display_string("coccia.valerio@gmail.com ", 2)
	sleep(1)
	display.lcd_clear()
	display.lcd_display_string("Telefono : ", 1)
	display.lcd_display_string("3451238135", 2)
	sleep(1)
	display.lcd_clear()

	while True:
		xxcoin=int(r.get("coin"))
		xxid=int(r.get("id"))
		xxcrediti=int(r.get("crediti"))
		xxgettoni=int(r.get("gettoni"))
		xxnome=(r.get("nome"))
		# An example of infinite scrolling text
		display.lcd_display_string("CPU : 50% ", 1)
		display.lcd_display_string("RAM : 50% ", 2)
		sleep(1)
		display.lcd_clear()


		display.lcd_display_string("MEMORIA : 50% ", 1)
		display.lcd_display_string("WIFI    : 50%", 2)
		sleep(1)
		display.lcd_clear()


		display.lcd_display_string("ID : ",1)
		display.lcd_display_string(str(xxid),2)
		sleep(2)
		display.lcd_clear()


		display.lcd_display_string("COIN : ",1)
		display.lcd_display_string(str(xxcoin),2)
		sleep(2)
		display.lcd_clear()

		display.lcd_display_string("CREDITI : ",1)
		display.lcd_display_string(str(xxcrediti),2)
		sleep(2)
		display.lcd_clear()

		display.lcd_display_string("GETTONI : ",1)
		display.lcd_display_string(str(xxgettoni),2)
		sleep(2)
		display.lcd_clear()

		display.lcd_display_string("NOME : ",1)
		display.lcd_display_string(str(xxnome),2)
		sleep(2)
		display.lcd_clear()


except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	display.lcd_clear()

















try:
        while True:
                if (count == 1):
                        GPIO.wait_for_edge(17, GPIO.FALLING)
                        counter += 1
                        print("Inseriti " +str(counter)+"/2")
                        #upCoinPlus1()
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












 

