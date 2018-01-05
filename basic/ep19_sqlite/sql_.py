import sqlite3
import sys


def printDB():
	try:
		result = theCursor.execute("SELECT ID, Fname, Lname, Age, Address, Salary, HireDate FROM Employees")

		for row in result:
			print("ID:", row[0])
			print("Fname:", row[1])
			print("Lname:", row[2])
			print("Age:", row[3])
			print("Address:", row[4])
			print("Salary:", row[5])
			print("HireDate:", row[6])
	except sqlite3.OperationalError:
		print("The table doesn't exist")
	except:
		print("Something is wrong")
db_conn = sqlite3.connect('test.db')
print("Database created")

theCursor = db_conn.cursor()

# delete table
db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()
# create table
try:
	db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Fname TEXT NOT NULL, Lname TEXT NOT NULL, Age INT NOT NULL, Address TEXT NOT NULL, Salary REAL, HireDate TEXT);")
	db_conn.commit()
	print("Table created")
except sqlite3.OperationalError:
	print("Can't create table")

db_conn.execute("INSERT INTO Employees (Fname, Lname, Age, Address, Salary, HireDate) VALUES ('Kristofferson', 'Carillo', 18, 'Angeles City', 18000, date('now'))")



try:
	db_conn.execute("UPDATE Employees SET Address='Catanauan' WHERE ID=1")
	db_conn.commit
except sqlite3.OperationalError:
	print("Table can't be updated")


# try:
# 	db_conn.execute("DELETE FROM Employees WHERE ID=1")
# 	db_conn.commit()
# except sqlite3.OperationalError:
# 	print("Table can't be deleted")

try:
	db_conn.execute("ALTER TABLE Employees ADD COLUMN 'Image' BLOB DEFAULT NULL")
	db_conn.commit()
except sqlite3.OperationalError:
	print("Table can't be updated")

printDB()

theCursor.execute("PRAGMA TABLE_INFO(Employees)")

rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]
print(rowNames)

theCursor.execute("SELECT COUNT(*) FROM Employees")
numOfRows = theCursor.fetchall()
print("Total Rows:", numOfRows[0][0])

theCursor.execute("SELECT SQLITE_VERSION()")
print("SQLite Version: ", theCursor.fetchone())



db_conn.close()
print("Database closed")
