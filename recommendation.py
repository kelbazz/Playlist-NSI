import sqlite3
import leo

conn = sqlite3.connect('chansons.db')
cursor = conn.cursor()



cursor.execute("SELECT * FROM chansons ORDER BY isrc ASC")

result = cursor.fetchall()
for lign in result:
    print(lign)

first_song = leo.chanson_depart
matrix = leo.matrice_transition