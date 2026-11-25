
import mysql.connector
from mysql.connector import Error

try:
    print("Connecting to database...")
    with mysql.connector.connect( # type: ignore[invalid-context-manager]
        host="localhost",
        port=3306,
        user="root",
        password="gokstad",
        database="world"
    ) as connection:  # ty: ignore[invalid-context-manager]
        print("Connected to MySQL")
        with connection.cursor() as cursor: # type: ignore[invalid-context-manager]  # ty: ignore[invalid-context-manager]
            sql = (
                "SELECT Name, Population "
                "FROM world.city "
                "WHERE CountryCode = 'NOR'"
            )
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                print("No results found")
            else:
                for name, population in rows:
                    print(f"Cityname: {name}, Population: {population}")
except Error as e:
    print(f"Error using MySQL: {e}")
