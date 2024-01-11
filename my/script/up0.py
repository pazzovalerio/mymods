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
                        cursor.execute("UPDATE crediti SET coin = 0  WHERE id = '1'")
                        cursor.execute("UPDATE crediti SET crediti = 0  WHERE id = '1'")
                        mydb.commit()
                        mydb.close()  
                        count = 1   
                        exit ()                       
except KeyboardInterrupt:
        exit ()











 

