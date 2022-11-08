import interface
from flask import Flask
from flask import render_template, request, url_for, flash, redirect

app = Flask(__name__,template_folder="templates")
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

@app.route('/',methods=('GET','POST'))
def index():
    values = 0
    if request.method == 'POST':
        gehalt = request.form['gehalt']
        steuersatz = request.form['steuersatz']

        if not gehalt:
            flash('Gehalt wird benötigt')
        elif not steuersatz:
            flash('Steuersatz wird benötigt')
        else:
            #values = {"gehalt":gehalt,"steuersatz":steuersatz}
            calculated_value_tax = float(gehalt) * (float(steuersatz)/100)
            calculated_value_tax = round(calculated_value_tax,2)
            return render_template("result.html",tax=calculated_value_tax)
    if request.method=="GET":
        return render_template("index.html")


@app.route('/result')
def result():
    return render_template("result.html",values=values)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1800,debug=True)

