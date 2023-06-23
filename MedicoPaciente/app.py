from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


#inicialización del servidor Flask
app= Flask(__name__)
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "consultorio"

app.secret_key= 'mysecretkey'

mysql= MySQL(app)

#----------------

@app.route('/')
def index():
    
    return render_template('Index.html')



#----------------

if __name__== '__main__':
    app.run(port= 4000, debug=True)