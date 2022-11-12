import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_basics"
)
mycursor =mydb.cursor()
# mycursor.execute("ALTER TABLE customers ADD COLUMN fav INT (255)")
sql="INSERT INTO products (id,name) VALUES(%s,%s,%s)"
val=[
    ('Peter', 'Lowstreet 4',154),
  ('Amy', 'Apple st 652',154),
  ('Hannah', 'Mountain 21',155),
  ('Michael', 'Valley 345',156),
  ('Sandy', 'Ocean blvd 2',158),
  ('Betty', 'Green Grass 1',154),

]

mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "records inserted.")

