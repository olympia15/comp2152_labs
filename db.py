import sqlite3
import functions

# connect to the database
db_connection = sqlite3.connect("sqlite.db")

# cursor to read through query results
db_cursor = db_connection.cursor()

# query
query = "SELECT * FROM demo"

# execute the query
# the cursor only returns one line
db_cursor.execute(query)

# fetchone() returns one row
print("Reading one row")
rows = db_cursor.fetchone()
print(rows)

# fetchmany() can take an argument such as a number referring to how many rows we want
print("Reading 3 rows")
rows = db_cursor.fetchmany(3)
print(rows)

# use fetchall() to retrieve everything
# notice the cursor moved after the above queries and continued where it left off
# print("Reading all rows")
# rows = db_cursor.fetchall()
# for row in rows:
#     print(row)
# can also be written in short form like this:
functions.query_responder(db_cursor, "fetchall") # this can also be done with fetchmany and fetchone

# to commit or save a change in the db, use commit()
# query2 = "INSERT INTO demo (Name, Hint) VALUES ('Michael', 'Murphy')"
# db_cursor.execute(query2)
# db_connection.commit()

# parameterized query
# do NOT use an f-string when adding inputs to a query
# id_num = input("Enter id: ")
# query3 = "SELECT * FROM demo WHERE ID > ?"
# db_cursor.execute(query3, id_num)
# functions.query_responder(db_cursor, "fetchall")