## IMPORTO LIBRERIE
import mysql.connector

## DEFINISCO VARIABILI GLOBALI
id_macchina = 1
id = 1
coin = 0
crediti = 0
nome = 'nome'
gettoni = 0




## DATI CONNESSIONE DATABASE remoto
mydb = mysql.connector.connect( 
    host = "159.203.136.91", 
    user = "photoboot1", 
    password = "minimoto", 
    database = "photoboot",
    )

