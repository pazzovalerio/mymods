# Importing module
import mysql.connector
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "minimoto",
    database = "photoboot",
)
 
# Printing the connection object
print(mydb)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor(buffered=True)
 
# Show database
cursor.execute("UPDATE crediti SET coin = 0  WHERE id = '1'")
cursor.execute("SELECT coin FROM crediti WHERE ID ='1'")
mydb.commit()
mydb.close()



 
for x in cursor:
  print(x)
