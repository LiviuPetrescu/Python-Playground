import mysql
import mysql.connector
class Animal:
    def __init__(self,nume,varsta):
        self.nume_animal = nume
        self.varsta_animal = varsta

    def numar_picioare(self,numar):
        self.nr_picioare=numar


animal1=Animal("Leu",1)
animal2= Animal("Tigru",5)

# print(animal1.nume_animal)
# print(animal1.varsta_animal)
# print(animal2.nume_animal)
# print(animal2.varsta_animal)
animal2.numar_picioare(4)
animal1.numar_picioare(3)
# print(animal1.nr_picioare)
# print(animal2.nr_picioare)


class Calculator():
    # class variable
    num = 100

    # constructor(daca nu il declaram unul default este creat de python)
    def __init__(self,a,b):
        #  instance variable
        self.variabila_a = a
        self.variabila_b = b

    def suma(self):
        return self.variabila_a + self.variabila_b

    def inmltire(self):
        return self.variabila_a + self.variabila_b + Calculator.num

numere_test = Calculator(5, 6)
print(numere_test.suma())




class Car:
    def __init__(self, speed, mileage):
        self.max_speed=speed
        self.car_mileage=mileage
model_cal=Car(169,200000)
# print(model_cal.car_mileage, model_cal.max_speed)

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