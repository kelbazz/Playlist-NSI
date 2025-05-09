import sqlite3

conn = sqlite3.connect('chansons.db')
cursor = conn.cursor()



cursor.execute("SELECT * FROM chansons ORDER BY isrc ASC")

result = cursor.fetchall()
for lign in result:
    print(lign)