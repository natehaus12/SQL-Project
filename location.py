import sqlite3

def insert(connection, cursor):
    name = input("Please Enter Your Name: ")
    location = input("Please Enter Your Location: ")
    print ("Success!")
    cursor.execute("INSERT INTO locationTable VALUES (?,?)", (name, location))
    connection.commit()
    connection.close()

def modify(connection, cursor):
    name = input("Pleae Enter Your Name: ")
    newLocation = input("Please Enter Your New Location: ")
    cursor.execute("UPDATE locationTable SET location = ? WHERE name = ?", (newLocation, name))
    print("Success")
    connection.commit()
    connection.close()

def query(connection, cursor):
    newName = input("Please Enter Your Name: ")
    cursor.execute("SELECT location FROM locationTable WHERE name = ?", [newName])
    result = cursor.fetchall()
    print("Your current location is: ")
    for i in range(len(result)):
        print(f"{result[i][0]}")

def delete(connection, cursor):
    delName = input("Please Enter the Name of the Person You Would Like to Delete: ")
    cursor.execute("DELETE FROM locationTable WHERE name = ?", [delName])
    print("Success")
    connection.commit()
    connection.close()


connection = sqlite3.connect('location.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS locationTable(name text, location text)''')


print("Welcome to the location Database, please choose what you would like to do.")
print("1: Add someone to the database.")
print("2: Modify an existing person")
print("3: View your current location.")
print("4: Delete from database")

selection = input()

if selection == '1':
    insert(connection, cursor)
elif selection == '2':
    modify(connection, cursor)
elif selection == '3':
    query(connection,cursor)
elif selection == '4':
    delete(connection,cursor)
else:
    print("Invalid Input")