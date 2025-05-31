import sqlite3
from datetime import datetime

# Connect to SQLite DB (or create if not exists)
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Create table (if not exists)
cursor.execute('''
CREATE TABLE IF NOT EXISTS hospital_records (
    patient_id TEXT PRIMARY KEY,
    name TEXT,
    dob TEXT,
    admission_date TEXT,
    diagnosis TEXT,
    doctor TEXT
)
''')

# Sample insert
record = ('P123456', 'Jane Doe', '1990-04-15', datetime.now().strftime('%Y-%m-%d'), 'Pneumonia', 'Dr. Smith')

# Insert record
cursor.execute('INSERT OR REPLACE INTO hospital_records VALUES (?, ?, ?, ?, ?, ?)', record)
conn.commit()
conn.close()

print("Hospital record inserted.")
