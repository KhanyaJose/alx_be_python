# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Function to create the alx_book_store database if it doesn't exist.
    """
    # Database connection configuration
    # Update these with your MySQL server credentials
    host = "localhost"
    user = "root"  # Change this to your MySQL username
    password = ""  # Change this to your MySQL password
    
    connection = None
    
    try:
        # Connect to MySQL server without specifying a database
        print("Connecting to MySQL server...")
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()
            
            # Create the database if it doesn't exist
            # Using IF NOT EXISTS to avoid errors if database already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            # Close cursor
            cursor.close()
            
    except Error as e:
        print(f"Error: {e}")
        print("Failed to connect to the MySQL server. Please check your credentials and ensure MySQL is running.")
        
    finally:
        # Close the connection if it was established
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()