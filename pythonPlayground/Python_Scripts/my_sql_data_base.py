import mysql
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vrajeala.06",
  database = "liviu_database"
)
mycursor = mydb.cursor()
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

# mycursor.execute("CREATE DATABASE Liviu_database")

# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print("1 record inserted, ID:", mycursor.lastrowid)

# mycursor.execute("SELECT * FROM customers")
#
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# mycursor.execute("SELECT name FROM customers")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers ORDER BY name"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) deleted")