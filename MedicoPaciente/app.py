from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

# Inicialización del servidor Flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "consultorio"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

# ----------------

@app.route('/ListaDr')
def ListaDr():
    return render_template('ListaDr.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method == 'POST':
        Vrfc = request.form['rfc']
        Vpassword = request.form['password']

    usu = {
    'RFCA1234': 'Admin1',
    'RFCM1234': 'Medico1',
    }

    if Vrfc == 'RFCA1234':
        if Vrfc in usu and usu[Vrfc] == Vpassword:
            session['rfc'] = Vrfc
            return redirect(url_for('ListaDr'))
        else: 
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('index'))
    elif Vrfc == 'RFCM1234':
        if Vrfc in usu and usu[Vrfc] == Vpassword:
            session['rfc'] = Vrfc
            return redirect(url_for('ListaDr'))
        else: 
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('index'))

# ----------------

if __name__ == '__main__':
    app.run(port=4000, debug=True)
