import sqlite3

# Create a connection to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Create the contacts table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        message TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
