import csv
import sqlite3


with open('./Lohnsteuertabelle.sql', 'r') as sqlFile:       #+ SQL Datei wird eingelesen und als "Script"-String
        sqlScript = sqlFile.read()                          #+ abgespeichert

try:
    con = sqlite3.connect("localDB.dat")                    #+ Versucht hier in diesen Try&Catch Block eine
    print("Connection Successful")                          #+ Datenbank zu erstellen und dann sich zu verbinden
except sqlite3.Error as error:
    print("Connection failed")

    cur = con.cursor()                                      #+ Ein Cursor Element, welches die Datenbank
                                                            #+ Befehle weiter an die Datenbank leitet

    cur.executescript(sqlScript)                            #+ Datenbank wird mithilfe der .sql Datei gefüllt

    #+readTable = cur.execute("SELECT * FROM Lohnsteuertabelle")                              #+ Alle Daten werden ausgelesen
    readTable = cur.fetchall()
    for i in readTable:
        print(i[None])

    cur.close()                                             #+ Cursor Element wird beendet
    con.close()                                             #+ Verbindung zur Datenbank wird beendet
