import mysql.connector 

database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '@Odogwuguyman1'

        )


cursorObject = database.cursor()


cursorObject.execute("CREATE DATABASE work")


print("All Done!")
