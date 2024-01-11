#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Example: Scrolling text on display if the string length is major than columns in display.
# Created by Dídac García.

# Import necessary libraries for communication and display use
import drivers
from time import sleep
from newfunction import *
from config import *
import redis
import os
import psutil
r = redis.Redis()

#xid = (datilcd[0])
#xcoin= (datilcd[1])
#xcred = (datilcd[2])
#xname = (datilcd[3])
#xgettoni = (datilcd[4])
# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Main body of code
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
		
		



except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	display.lcd_clear()
