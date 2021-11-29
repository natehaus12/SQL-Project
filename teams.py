import sqlite3

def insert(connection, cursor):
    name = input("Please Enter Your Name: ")
    team = input("Please Enter Your Favorite Team: ")
    print ("Success!")
    cursor.execute("INSERT INTO footballTable VALUES (?,?)", (name, team))
    connection.commit()
    connection.close()

def modify(connection, cursor):
    name = input("Pleae Enter Your Name: ")
    newTeam = input("Please Enter Your New Favorite Team: ")
    cursor.execute("UPDATE footballTable SET favTeam = ? WHERE name = ?", (newTeam, name))
    print("Success")
    connection.commit()
    connection.close()

def query(connection, cursor):
    newName = input("Please Enter Your Name: ")
    cursor.execute("SELECT favTeam FROM footballTable WHERE name = ?", [newName])
    result = cursor.fetchall()
    print("Your favorite team is: ")
    for i in range(len(result)):
        print(f"{result[i][0]}")

def delete(connection, cursor):
    delName = input("Please Enter the Name of the Person You Would Like to Delete: ")
    cursor.execute("DELETE FROM footballTable WHERE name = ?", [delName])
    print("Success")
    connection.commit()
    connection.close()


connection = sqlite3.connect('teams.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS footballTable(name text, favTeam text)''')


print("Welcome to the football Database, please choose what you would like to do.")
print("1: Add someone to the database.")
print("2: Modify an existing person")
print("3: View your favorite team.")
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