from config import *

def up0Rem():
    cursor = mydbRem.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET coin = 0  WHERE id = '1'")
    cursor.execute("UPDATE crediti SET crediti = 0  WHERE id = '1'")
    mydbRem.commit()
    cursor.close()
    mydbRem.close()
    #exit ()

def readRem(idr):
    global rows
    global id
    global coin
    global crediti
    cursor = mydbRem.cursor(buffered=True)
    
    #Reading the Employee data      
    cursor.execute("select * from crediti")  
      #fetching the rows from the cursor object  
    rows = cursor.fetchall()
    user = rows[idr -1] 
    id = user[0]
    coin = user[1]
    crediti = user[2]
    print(rows,id,coin,crediti)
    mydbRem.commit() 
    cursor.close()     
    mydbRem.close()
 
    return(id,coin,crediti)
    #raise
    #exit()
    #return mydbRem







def upRem():
    cursor = mydbRem.cursor(buffered=True)
    cursor.execute("UPDATE crediti SET crediti = crediti +1  WHERE id = '1'")
    mydbRem.commit()
    #mydb.close()  
    #exit ()
