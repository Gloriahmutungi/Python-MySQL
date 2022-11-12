import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_basics"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM customers limit 5"
# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
mycursor.execute("SELECT * FROM customers limit 5 OFFSET 2")

myresult=mycursor.fetchall()

for x in myresult:
  print(x)