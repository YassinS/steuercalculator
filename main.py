import interface
from flask import Flask
from flask import render_template, request, url_for, flash, redirect

app = Flask(__name__,template_folder="templates")
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

@app.route('/',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        gehalt = request.form['IB_Brutto']
        steuerklasse = request.form['IB_Steuerklasse']
        try:
            kirche = request.form.get('Kirche') 
        except Exception:
            kirche = False
        if not gehalt:
            flash('Gehalt wird benötigt')
        elif not steuerklasse:
            flash('Steuerklasse wird benötigt')
        else:
            calculated_value_tax = float(gehalt) * (float(steuerklasse)/100)
            calculated_value_tax = round(calculated_value_tax,2)
            if kirche:
                kirchensteuer = round(float(gehalt) * 0.09,2)
                values = {"gehalt":gehalt,"steuerklasse":steuerklasse,"kirche":kirche,"kirchensteuer":kirchensteuer}
            else:
                
                values = {"gehalt":gehalt,"steuerklasse":steuerklasse,"kirche":"Nein"}
            return render_template("result.html",tax=calculated_value_tax,values=values)
    if request.method=="GET":
        return render_template("index.html")


@app.route('/result')
def result():
    return render_template("result.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1800,debug=True)

