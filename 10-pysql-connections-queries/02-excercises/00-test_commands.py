# # TEST if MySQL Connector is installed
# try:
#     import mysql.connector
# except:
#     print("Import failed")
# else:
#     print("MySQL is ready!")

import mysql.connector
from mysql.connector import Error

try:
    print("Connecting to the database...")
    with mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="gokstad",
        database="world"
    ) as connection:  # ty: ignore[invalid-context-manager]
        print("Connected to MySQL!")
except Error as e:
    print(f"Error using MySQL: {e}")

