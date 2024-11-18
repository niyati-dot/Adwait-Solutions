import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'niya'

)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE  database adwait")
print("All done")