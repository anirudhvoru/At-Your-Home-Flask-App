import sqlite3

# Open a connection to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
c = conn.cursor()

# Execute the SQL query to delete all rows from the users table
c.execute('DELETE FROM users')

# Execute the SQL query to delete all rows from the contacts table
c.execute('DELETE FROM contacts')

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
