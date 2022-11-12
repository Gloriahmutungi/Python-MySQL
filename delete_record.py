import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_basics"
)
mycursor =mydb.cursor()

# sql = "DELETE FROM customers WHERE address='Westlands' "
# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted successfully")

#prevent mysql injection which is a common web hacking technique to misuse your database

sql="DELETE FROM customers WHERE address=%s"
adr=("Green Grass 1", )

mycursor.execute(sql,adr)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted successfuly")