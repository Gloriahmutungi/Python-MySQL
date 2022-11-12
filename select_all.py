import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_basics"
)
mycursor =mydb.cursor()
mycursor.execute("SELECT name,address FROM customers")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)

# #using fetch one method which returns the firstr row of the result
# myresult = mycursor.fetchone()
# print(myresult)

