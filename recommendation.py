import sqlite3

# Connexion à la base de données (elle sera créée si elle n'existe pas)
conn = sqlite3.connect('chansons.db')
cursor = conn.cursor()



# Insérer une donnée
cursor.execute("SELECT * FROM chansons")

resultats = cursor.fetchall()
for ligne in resultats:
    print(ligne)