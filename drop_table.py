import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password="",
    database = "python_basics"
)
mycursor = mydb.cursor()

sql ="DROP TABLE test"
mycursor.execute(sql)

