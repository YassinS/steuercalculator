from flask import Flask
from flask import render_template, request, url_for, flash, redirect
import csv
import sys



app = Flask(__name__,template_folder="templates")

def check_csv(gehalt,steuerklasse):
    with open("Lohnsteuertabelle.csv") as csvfile:
        rows = csv.reader(csvfile,delimiter=";")
        for row in rows:
            if gehalt in row:
                return row
            else:
                if int(row[0])>=int(gehalt):
                    return row

@app.route('/',methods=('GET','POST'))
def index():
    wrong_values = 0
    if request.method == 'POST':
        lohnsteuer = 0
        gehalt = request.form['IB_Brutto']
        steuerklasse = request.form['IB_Steuerklasse']
        try:
            kirche = request.form.get('Kirche') 
        except Exception:
            kirche = False
        if int(steuerklasse) > 0 and int(steuerklasse) <7:
            lohnsteuer=check_csv(gehalt,steuerklasse)[int(steuerklasse)]
        else:
            wrong_values=1
        
        if kirche:
            kirchensteuer = round(float(gehalt) * 0.09,2)
            values = {"gehalt":gehalt,"steuerklasse":steuerklasse,"kirche":kirche,"kirchensteuer":kirchensteuer}
        else:
            values = {"gehalt":gehalt,"steuerklasse":steuerklasse,"kirche":"Nein"}
        print(wrong_values)
        return render_template("index.html",error=wrong_values,tax=lohnsteuer,values=values,gehalt_input=gehalt,steuerklasse_input=steuerklasse)
    if request.method=="GET":
        return render_template("index.html",error=wrong_values,tax=0,gehalt_input="",steuerklasse_input="")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1800,debug=True)

