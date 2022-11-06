import psycopg2
from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # the cursor for perfoming database operations
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

    # create a new table
    with connection.cursor() as cursor:
        cursor.execute(

        """CREATE TABLE shell_and_bus(
           drawing varchar(50) NOT NULL unique ,
            type varchar(50) ,
            size varchar(50) ,
            diameter varchar(50) NOT NULL,
            PRIMARY KEY (drawing));"""

        """CREATE TABLE detail_size(
            drawing varchar(50) NOT NULL unique,
            size varchar(50) NOT NULL ,
            note varchar(50),
            PRIMARY KEY (drawing));"""

        """CREATE TABLE summary_list_C(
            name varchar(50) NOT NULL,
            drawing varchar(50) NOT NULL unique,
            material varchar(50) ,
            amount varchar(50) NOT NULL,
            PRIMARY KEY (drawing),
            FOREIGN KEY (drawing) REFERENCES shell_and_bus(drawing),
            FOREIGN KEY (drawing) REFERENCES detail_size(drawing));"""
        )

        connection.commit()
        print("[INFO] Table created successfully")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")