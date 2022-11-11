import csv
import sqlite3

try:
    con = sqlite3.connect("Lohnesteuertabelle.sql")         #+ Versucht hier in diesen Try&Catch Block eine
    print("Connection Successful")                          #+ Verbindung zur Datenbank herzustellen
except sqlite3.Error as error:
    print("Connection failed")

    cur = con.cursor()                                      #+ Ein Cursor Element, welches die Datenbank
                                                            #+ Befehle weiter an die Datenbank leitet

    readDB = cur.fetchall()                                 #+ Liest einfach alles aus der Datenbank aus

    for i in readDB:                                        
        print(i[None])

    cur.close()                                             #+ Cursor Element wird beendet
    con.close()                                             #+ Verbindung zur Datenbank wird beendet
