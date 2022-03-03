import mysql.connector 
from mysql.connector import Error

try:
    db=mysql.connector.connect(
        host="localhost",
        user="pythonconnect",
        database="pythonconnect",
        )

    sqlQueries = """CREATE TABLE Laptop ( Id int(11) NOT NULL,Name varchar(250) NOT NULL,Price float NOT NULL,Purchase_date Date NOT NULL,PRIMARY KEY (Id)) """
    deleteTable = """DROP TABLE Laptop"""

    cursor = db.cursor()
    cursor.execute(sqlQueries)

except Error as error:
    print("Failed To Connect to Database", error)

finally:
    if db.is_connected():
        cursor.close()
        db.close()
        print("MySQL Connection Closed")
