import csv
import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

with open('Lohnsteuertabelle.csv', 'r') as importedTable:
    dr = csv.DictReader(importedTable)

    for i in dr:
        #+print(i[None][0])
        cur.executemany(f"INSERT INTO t ({i[None][0][0]}, {i[None][0][1]}, {i[None][0][2]}, {i[None][0][3]}, {i[None][0][4]}, {i[None][0][5]}, {i[None][0][6]}) VALUES('inEuro', 'sk1', 'sk2', 'sk3', 'sk4', 'sk5', 'sk6' );", importedTable)
        cur.execute("SELECT * from t")
    con.commit()
    con.close()
