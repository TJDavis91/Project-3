import sqlite3

conn = sqlite3.connect('Currency_db.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Bitcoin LIMIT 5;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()