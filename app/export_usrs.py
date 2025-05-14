import sqlite3
import csv

# Path to your database
DB_PATH = 'site.db'  # or update if it's elsewhere

# Output CSV filename
CSV_FILE = 'users_export.csv'

# Connect to SQLite DB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Query user table
cursor.execute("SELECT id, name, dob, gender FROM user")
rows = cursor.fetchall()

# Column names
headers = [description[0] for description in cursor.description]

# Write to CSV
with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # header
    writer.writerows(rows)

conn.close()

print(f"[✔] Exported {len(rows)} rows to {CSV_FILE}")
