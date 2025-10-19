# Write a simple python script that creates the database alx_book_store in your MySQL server.

# Name of python script should be MySQLServer.py
# If the database alx_book_store already exists, your script should not fail
# You are not allowed to use the SELECT or SHOW statements
# NOTE :

# Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

# Print error message to handle errors when failing to connect to the DB.

# handle open and close of the DB in your script.

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Eli@2020',
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")
    
    mycursor.execute("USE alx_book_store;")
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
    print(f'An error occured: {e}')


def run_sql_file(filename):
    with open(filename, 'r') as sql_file:
        sql_commands = sql_file.read()

# split commands by semicolon and execute each

    for command in sql_commands.split(';'):
        command = command.strip()
        if command:
            try:
                mycursor.execute(command)

                # If it's a SELECT query, fetch and print results
                if command.upper().startswith("SELECT"):
                    _ = mycursor.fetchall() 
                    results = mycursor.fetchall()
                    for row in results:
                        print(row)

            except Exception as e:
                print(f"Error executing command: {command}\n{e}")


run_sql_file('task_2.sql')
run_sql_file('task_3.sql')
run_sql_file('task_4.sql')
run_sql_file('task_5.sql')
run_sql_file('task_6.sql')
# Close connection to the databasse  
mycursor.close()
mydb.close()
