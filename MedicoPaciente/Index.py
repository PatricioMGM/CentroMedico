users = {
    'diego': 'diego1',
    'administrador': 'administrador1',
    'ejecutivo': 'ejecutivo1'
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == 'diego':
    if username in users and users[username] == password:
        session['username'] = username

        print("Consultar tu Informacion Personal y/o Reservacion\n")
        print("Consulta tu informacion: <a href=ConsultaPasajero.php?>Click Aqui</a>\n")
        print("Consulta tu reservacion: <a href=ConsultaReservacionS.php?>Click Aqui</a>\n\n\n")
        print("Altas, Bajas y Actualizacion tu informacion\n\n")
        print("Informacion personal: <a href=IEAPasajero.php?>Click Aqui</a>\n")
        print("Informacion de tu reservacion: <a href=IEAReservacionS.php?>Click Aqui</a>")
    else:
        print("Usuario o contraseña incorrectos.")
