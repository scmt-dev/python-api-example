# import db
# import mariadb

# def add_data(email, password):
#     try:
#         statement = "INSERT INTO users (email, password) VALUES (%s, %s)"
#         data = (email, password)
#         db.cur.execute(statement, data)
#         db.con.commit()
#         print("Successfully added entry to database")
#     except mariadb.Error as e: 
#         print(f"Error: {e}")

# add_data("usertest@email.com", "1234")