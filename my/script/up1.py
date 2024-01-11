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
                        cursor.execute("UPDATE crediti SET coin = coin + 1  WHERE id = '1'")
                        mydb.commit()
                        mydb.close()  
                        count = 1   
                        exit ()                       
except KeyboardInterrupt:
        exit ()











 

