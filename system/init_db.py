import sqlite3

conn = sqlite3.connect('gym.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    captain TEXT,
    amount_paid REAL,
    notes TEXT,
    sub_from TEXT,
    sub_to TEXT
)
''')

conn.commit()
conn.close()

print("✅ Database initialized successfully.")
