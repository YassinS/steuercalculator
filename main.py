from flask import Flask
from flask import render_template, request,jsonify
import csv

app = Flask(__name__,template_folder="templates")

def check_csv(gehalt):
    with open("Lohnsteuertabelle.csv") as csvfile:
        gehalt = float(gehalt)
        rows = csv.reader(csvfile,delimiter=";")
        for row in rows:
            if gehalt>70000:
                rows = list(rows)
                return rows[-1]
            if gehalt in row:
                return row
            else:
                if float(row[0])>=gehalt:
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
        elif float(gehalt)< 0:
            wrong_values = 2
        elif float(gehalt) < 9984:
            lohnsteuer = 0
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

        #calculate salary
        tax = float(float(gehalt)-int(lohnsteuer)-kirchensteuer)

        #replace . with ,
        tax = str(tax).replace(".",",")

        #check for comma numbers
        if len(tax.split(",")[1]) < 2:
            #add 0
            tax = tax + "0"

        #return index.html with values    
        return render_template("index.html",error=wrong_values,tax=tax,gehalt_input=gehalt,steuerklasse_input=steuerklasse,kirche=kirche_tf)
    if request.method=="GET":
        #return index.html with default values 
        return render_template("index.html",error=wrong_values,tax=0,gehalt_input="",steuerklasse_input=1,kirche=0) 


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# API        

#@app.route("/get_income_tax/<int:gehalt>/<int:lohnsteuer>/")
#def get_income_tax_post():
#    result = check_csv(gehalt)[lohnsteuer]
#     return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1800,debug=True)

