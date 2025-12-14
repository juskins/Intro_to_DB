import mysql.connector
from mysql.connector import Error

DB_NAME = 'alx_book_store'

try:
    # Connect to MySQL server (update user and password as needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Change this if your MySQL user is different
        password=''   # Change this if your MySQL password is not empty
    )
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Database '{DB_NAME}' created successfully!")
        except Error as e:
            print(f"Failed to create database: {e}")
        finally:
            cursor.close()
    else:
        print("Failed to connect to MySQL server.")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
