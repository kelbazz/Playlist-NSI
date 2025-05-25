import sqlite3
import leo
from classes import *

conn = sqlite3.connect("chansons.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM chansons ORDER BY isrc ASC")

result = cursor.fetchall()
for lign in result:
    new_song = CHANSON(isrc=lign[0], title=[1], artist=[2], time=[3], im=[4])
    new_node = Node(new_song, False)


first_song = leo.chanson_depart
matrix = leo.matrice_transition
