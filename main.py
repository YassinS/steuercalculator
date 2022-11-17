from flask import Flask
from flask import render_template, request
import csv
import sys

app = Flask(__name__,template_folder="templates")

def check_csv(gehalt):
    with open("Lohnsteuertabelle.csv") as csvfile:
        rows = csv.reader(csvfile,delimiter=";")
        for row in rows:
            if int(gehalt)>70000:
                rows = list(rows)
                return rows[-1]
            if gehalt in row:
                return row
            else:
                if int(row[0])>=int(gehalt):
                    return row

@app.route('/',methods=('GET','POST'))
def index():
    wrong_values = 0
    lohnsteuer = 0

    if request.method == 'POST':
        #get request form
        gehalt = request.form['IB_Brutto']
        steuerklasse = request.form['IB_Steuerklasse']
        kirche = request.form.get('CB_Kirche') 

        #check tax class
        if int(steuerklasse) < 0 and int(steuerklasse) >7:
            wrong_values=1
        elif int(gehalt)< 0:
            wrong_values = 2
        else:
            check = check_csv(gehalt)
            lohnsteuer=check[int(steuerklasse)]
        
        
        #check church tax
        if kirche:
            #calculate church tax 
            kirchensteuer = round(float(lohnsteuer) * 0.09,2)

            #church checkbox true
            kirche_tf = 1

        else:
            #no church tax
            kirchensteuer = 0

            #church checkbox false
            kirche_tf = 0

        #return index.html with values    
        return render_template("index.html",error=wrong_values,tax=int(int(gehalt)-int(lohnsteuer)-kirchensteuer),gehalt_input=gehalt,steuerklasse_input=steuerklasse,kirche=kirche_tf)
    if request.method=="GET":
        #return index.html with default values 
        return render_template("index.html",error=wrong_values,tax=0,gehalt_input="",steuerklasse_input=1,kirche=0) 
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1800,debug=True)

