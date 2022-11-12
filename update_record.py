import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_basics"
)
mycursor = mydb.cursor()

sql = "UPDATE customers set address='Westlands' WHERE address='Yellow Garden 2' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "row(s) affected")