# Importing module
import RPi.GPIO as GPIO
import time


# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'










GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 1

try:
        while True:
                if (count == 1):
                        import mysql.connector
                                # Creating connection object
                        mydb = mysql.connector.connect(
                                host = "localhost",
                                user = "root",
                                password = "minimoto",
                                database = "photoboot",
                        )               
                        cursor = mydb.cursor(buffered=True)
                                # Show database
                        cursor.execute("UPDATE crediti SET coin = coin + 2  WHERE id = '1'")
                        mydb.commit()
                        mydb.close()  
                        count = 1   
                        exit ()                       
except KeyboardInterrupt:
        GPIO.cleanup()
        exit ()











 

