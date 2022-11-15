import interface
from flask import Flask
from flask import render_template, request, url_for, flash, redirect
import csv
import sys



app = Flask(__name__,template_folder="templates")

def check_db(gehalt,steuerklasse):
    cur = interface.db()
    res = cur.execute(f"SELECT {int(steuerklasse)} FROM lohnsteuer WHERE 'in Euro'>{gehalt}")
    return res
def check_csv(gehalt,steuerklasse):
    with open("Lohnsteuertabelle.csv") as csvfile:
        rows = csv.reader(csvfile,delimiter=";")
        for row in rows:
            if gehalt in row:
                return row
            else:
                for i in row:
                    if int(i)>int(gehalt):
                        return row

@app.route('/',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        gehalt = request.form['IB_Brutto']
        steuerklasse = request.form['IB_Steuerklasse']
        try:
            kirche = request.form.get('Kirche') 
        except Exception:
            kirche = False
        lohnsteuer=check_csv(gehalt,steuerklasse)[int(steuerklasse)]
        if kirche:
            kirchensteuer = round(float(gehalt) * 0.09,2)
            values = {"gehalt":gehalt,"steuerklasse":steuerklasse,"kirche":kirche,"kirchensteuer":kirchensteuer}
        else:
            values = {"gehalt":gehalt,"steuerklasse":steuerklasse,"kirche":"Nein"}
        print(lohnsteuer)
        return render_template("index.html",tax=lohnsteuer,gehalt_input=gehalt,steuerklasse_input=steuerklasse)
    if request.method=="GET":
        return render_template("index.html",tax=0,gehalt_input="",steuerklasse_input="")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1800,debug=True)

