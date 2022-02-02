import sys
import json
import mariadb


try: con = mariadb.connect( 
    user="root", 
    password="test", 
    host="127.0.0.1", 
    database="api" 
)

except mariadb.Error as ex: 
    print(f"An error occurred while connecting to MariaDB: {ex}") 
    sys.exit(1) 
# Get Cursor 

cur = con.cursor()


# cur.execute("INSERT INTO users (email, password) VALUES ('test@gmail.com', '1234')")

# con.commit()

# def add_data(email, password):
#     try:
#         statement = "INSERT INTO users (email, password) VALUES (%s, %s)"
#         data = (email, password)
#         cur.execute(statement, data)
#         con.commit()
#         print("Successfully added entry to database")
#     except mariadb.Error as e: 
#         print(f"Error: {e}")

# add_data("user@email.com", "1234")

