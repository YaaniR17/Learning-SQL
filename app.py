import sqlite3

# Connecting to sqlite databse
connection_obj = sqlite3.connect('hantavirus.db')

# cursor object
cursor_obj = connection_obj.cursor()

# to select all column we will use
statement = '''SELECT * FROM patients'''

#cursor_obj.execute(statement)

#print("All the data")
output = cursor_obj.fetchall()
for row in output:
  print(row)

connection_obj.commit()

# Close the connection
connection_obj.close()