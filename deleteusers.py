import sqlite3

# Open a connection to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
c = conn.cursor()

# Execute the SQL query to delete all rows from the table
c.execute('DELETE FROM users')

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
