# ./app/app.py

#
# ────────────────────────────────────────────────────────────
#   :::::: app.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────
#
# Práctica 2 de DAI: Plantillas, Manejo de Sesiones y Frameworks CSS
# Autor: Juan Antonio Villegas Recio
# Curso 2021-2022
# Universidad de Granada

# Fichero CONTROLADOR que contiene la interación entre el modelo y la vista

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
import math
import re
import random

from flask.json import dumps
from model import Database
from modelMongoDB import DatabaseMongoDB
from flask import Flask, render_template, flash, render_template, request, session, jsonify
from pymongo import MongoClient
import json
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo



#
# ────────────────────────────────────────────────────────────────────────────────────────────────────────
#   :::::: E J E R C I C I O S   D E   L A   P R A C T I C A   1 : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────────────────────────────
#

# ─── EJERCICIO 1 ────────────────────────────────────────────────────────────────


# ─── EJERCICIO 1.1 ──────────────────────────────────────────────────────────────

# Hello World   
@app.route('/hello')
def hello():
    users = [ 'Rosalia','Adrianna','Victoria' ]
    return render_template('hello.html', title='Welcome', members=users, ejercicio=1)


# ─── EJERCICIO 1.2 ────────────────────────────────────────────────────────────────

# Ordenacion
# `lista` es una cadena de caracteres de numeros separados por espacios
# Por ejemplo: 5 2 7 3 10 9
def ordena_lista(lista):
    lista = lista.split()
    map_object = map(int, lista)
    lista = list(map_object)
    lista_original = [i for i in lista]
    for num_pasada in range(len(lista)-1,0,-1):
        for i in range(num_pasada):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return "Lista original: " + str(lista_original) + " Lista ordenada: " + str(lista)

@app.route('/ordena', methods=['GET', 'POST'])
def ordena():
    res = None
    if request.method == 'POST':
        numeros = request.form['lista']
        res = ordena_lista(numeros)
    
    return render_template('hello.html', res = res, ejercicio = 2)


# ─── EJERCICIO 1.3 ────────────────────────────────────────────────────────────────

# Criba de Eratóstenes
def criba_numero(n):
    lista = [i for i in range(2, n)]
    for i in range(2, int(math.sqrt(n))):
        for j in range(int(n/i)):
            if(i*j in lista):
                lista.remove(i*j)
    return str(lista)

@app.route('/criba', methods=['GET', 'POST'])
def criba():
    res = None
    if request.method == 'POST':
        numero = request.form['numero']
        res = criba_numero(int(numero))
    
    return render_template('hello.html', res = res, ejercicio = 3)


# ─── EJERCICIO 1.4 ────────────────────────────────────────────────────────────────

# Sucesión de Fibonacci
# Función que calcula el n-ésimo término de la sucesión de Fibonacci
def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/fibonacci')
def fibonacci_from_file():
    f = open("./files/numero.txt", "r")
    n = int(f.read())
    f.close()
    res = fibonacci(n)
    f = open("./files/salida.txt", "w")
    f.write(str(res))
    f.close()
    return "El resultado es " + str(res) + " y está almacenado en files/salida.txt"


# NOTE: A partir del ejercicio 4 no se han implementado enlaces en el menú desplegable
# de la web de la práctica 2.


# ─── EJERCICIO 1.5 ────────────────────────────────────────────────────────────────

# Corchetes
# Función que comprueba si la secuencia de corchetes está o no balanceada.
def secuencia_balanceada(secuencia):
    balanceada = False
    cerrado_sin_abrir = False
    n_corchetes = 0
    for c in secuencia:
        if(c == "["):
            n_corchetes += 1
        else:
            n_corchetes -= 1

        if(n_corchetes < 0):
            balanceada = False
            cerrado_sin_abrir = True
        elif (n_corchetes == 0):
            balanceada = True
        else:
            balanceada = False
    if(balanceada and not cerrado_sin_abrir):
        return True
    else:
        return False

# Función que genera una secuencia aleatoria de corchetes de longitud `len`
def genera_secuencia(len):
    sec = ""
    for i in range(len):
        if(random.randint(0,2)):
            car = "["
        else:
            car = "]"
        sec += car
    return sec

@app.route('/corchetes/<int:longitud>')
def corchetes(longitud):
    sec = genera_secuencia(longitud)
    if(secuencia_balanceada(sec)):
        return "La secuencia " + sec + " está balanceada"
    else:
        return "La secuencia " + sec + " no está balanceada"


# ─── EJERCICIO 1.6 ────────────────────────────────────────────────────────────────

# Verificar email
@app.route('/verifica_email/<string:email>')
def verifica_email(email):
    patron = "\w+@(hotmail|gmail|ugr|outlook)\.(com|es)"
    result = re.match(patron, email)
    if(result != None):
        return email + " es un correo electrónico"
    else:
        return email + " NO es un correo electrónico"

# ────────────────────────────────────────────────────────────────────────────────


# ─── EJERCICIO 2 ────────────────────────────────────────────────────────────────

# Renderizar una página con una imagen
@app.route('/imagen')
def imagen():
    return render_template('imagen.html')


# ─── EJERCICIO 3 ────────────────────────────────────────────────────────────────

# Error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


#
# ──────────────────────────────────────────────────────────────────────────────────────────────────
#   :::::: P Á G I N A S   D E   L A   P R A C T I C A   2 : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────────────────────
#

# A partir de aquí se encuentra el código propio de la práctica 2

# ─── INDEX ──────────────────────────────────────────────────────────────────────
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# ─── LOG IN ──────────────────────────────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    status = 0
    db = Database()
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        if(not db.comprobar_login(username, passwd)):
            status = -1
            flash('El usuario no existe o la contraseña no es correcta', 'error')
        else:
            status = 1
            session['username'] = username
            flash('Bienvenido ' + username + "!")

    return render_template('login.html', status = status)


# ─── LOG OUT ─────────────────────────────────────────────────────────────────────
@app.route('/logout')
def logout():
    session['username'] = None
    return render_template('logout.html')


# ─── SIGN UP ────────────────────────────────────────────────────────────────────
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    status = 0
    db = Database()
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        db.anadir_usuario(username, passwd, name, email, phone)
        flash('Bienvenido a bordo ' + username + "!")
        status = 1

    return render_template('signup.html', status = status)


# ─── PERFIL ─────────────────────────────────────────────────────────────────────
@app.route('/profile')
def profile():
    status = 0
    user = None
    db = Database()
    if('username' in session):
        user = db.buscar_usuario(session['username'])
        if(user != None):
            status = 1
            flash('Hola ' + user['username'] + ', aquí tienes tus datos:')
        else:
            status = -1
            flash('No se ha encontrado en la BD el usuario ' + session['username'], 'error')
    else:
        status = -1
        flash('No hay ningún usuario con sesión iniciada', 'error')
    return render_template('profile.html', status = status, user = user)


# ─── MODIFICAR DATOS DE USUARIO ─────────────────────────────────────────────────
@app.route('/modify', methods=['GET', 'POST'])
def modify_user():
    status = 0
    user = None
    db = Database()
    if 'username' in session:
        username = session['username']
        user = db.buscar_usuario(username)
        if request.method == 'POST' and user != None:
            new_name = request.form['name']
            new_email = request.form['email']
            new_phone = request.form['phone']
            user = db.modificar_usuario(username, new_name, new_email, new_phone)
            flash('Tus datos han sido cambiados!')
            return render_template('profile.html', status = 1, user = user )

        elif user == None:
            flash('No se ha encontrado al usuario ' + username, 'error' )
            status = -1
    else:
        flash('No hay ningún usuario con sesión iniciada', 'error')
        status = -1

    return render_template('modify_user.html', status = status, user = user)


# ─── AFTER REQUEST ──────────────────────────────────────────────────────────────
# Tras cada petición se ejecuta esta función que almacena en `session` las url de 
# las últimas tres páginas visitadas.
@app.before_request
def store_visited_urls():
    if("/static" not in request.url):           # Ignora las peticiones a bootstrap
        add_url_to_session(request.base_url)

# Función que añade una url a la variable `session`
def add_url_to_session(page):
    if('urls' in session):
        session['urls'].append((page, page[22:]))
        if(len(session['urls'])) > 3:
            session['urls'].pop(0)
    else:
        session['urls'] = [(page, page[22:])]
    session['urls'] = session['urls']


# ─── PRACTICA 3 ─────────────────────────────────────────────────────────────────


@app.route('/busca_coleccion', methods=['GET', 'POST'])
def busca_coleccion():
    status = 0
    lista_episodios = []
    episodios = db.samples_friends

    temporadas = ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', 'Season 6', 'Season 7', 'Season 8', 'Season 9', 'Season 10', ]

    if request.method == 'POST':
        temporada = int(request.form['temporada'].split()[1])
        for episodio in episodios.find({"season": temporada}):
            lista_episodios.append(episodio)
        status = 1

    return render_template('lista.html', status = status, episodios = lista_episodios, temporadas = temporadas)


@app.route('/episodio', methods=['GET'])
def busca_episodio():
    params = request.get_json()

    if params == None or 'busqueda' not in params:
        return "Error: Formato incorrecto", 400
    else:
        nombre = ""
        if 'nombre' in params['busqueda']:
            nombre = params['busqueda']['nombre']
        db = DatabaseMongoDB()
        episodios, status = db.busca_episodios_nombre(nombre)
        
        return jsonify(episodios), status

@app.route('/episodio', methods=['POST'])
def anade_episodio():
    params = request.get_json()
    if params == None:
        return "Error: No se ha encontrado fichero de entrada", 400
    elif 'anadir' not in params:
        return "Error: El fichero de entrada no tiene el formato correcto", 400
    else:
        args = {}
        if 'id' in params['anadir']:
            args['id'] = params['anadir']['id']
        if 'url' in params['anadir']:
            args['url'] = params['anadir']['url']
        if 'name' in params['anadir']:
            args['name'] = params['anadir']['name']
        if 'season' in params['anadir']:
            args['season'] = int(params['anadir']['season'])
        if 'number' in params['anadir']:
            args['number'] = int(params['anadir']['number'])
        if 'airdate' in params['anadir']:
            args['airdate'] = params['anadir']['airdate']
        if 'airtime' in params['anadir']:
            args['airtime'] = params['anadir']['airtime']
        if 'airstamp' in params['anadir']:
            args['airstamp'] = params['anadir']['airstamp']
        if 'runtime' in params['anadir']:
            args['runtime'] = int(params['anadir']['runtime'])
        if 'image' in params['anadir']:
            args['image'] = params['anadir']['image']
        if 'summary' in params['anadir']:
            args['summary'] = params['anadir']['summary']

        db = DatabaseMongoDB()
        salida = jsonify( "Se ha añadido un nuevo episodio:  " + db.anade_episodio(args))
        return salida, 200

@app.route('/episodio', methods=['PUT'])
def modifica_episodio():
    params = request.get_json()
    if params == None:
        return "Error: No se ha encontrado fichero de entrada", 400
    elif 'modificar' not in params:
        return "Error: El fichero de entrada no tiene el formato correcto", 400
    elif 'id' not in params['modificar']:
        return "Error: No se ha especificado el id del episodio a modificar", 400
    else:
        id_episodio = int(params['modificar']['id'])
        args = { 'id' : id_episodio }
        if 'url' in params['modificar']:
            args['url'] = params['modificar']['url']
        if 'name' in params['modificar']:
            args['name'] = params['modificar']['name']
        if 'season' in params['modificar']:
            args['season'] = int(params['modificar']['season'])
        if 'number' in params['modificar']:
            args['number'] = int(params['modificar']['number'])
        if 'airdate' in params['modificar']:
            args['airdate'] = params['modificar']['airdate']
        if 'airtime' in params['modificar']:
            args['airtime'] = params['modificar']['airtime']
        if 'airstamp' in params['modificar']:
            args['airstamp'] = params['modificar']['airstamp']
        if 'runtime' in params['modificar']:
            args['runtime'] = int(params['modificar']['runtime'])
        if 'image' in params['modificar']:
            args['image'] = params['modificar']['image']
        if 'summary' in params['modificar']:
            args['summary'] = params['modificar']['summary']

        db = DatabaseMongoDB()
        result = json.loads(db.modifica_episodio(args))
        if (result['ok'] == 1.0):
            salida = "Se ha modificado el episodio de id " + str(id_episodio) + "  "
            episodio = db.busca_episodio_id(id_episodio)
            if episodio != None:
                episodio = episodio[0]
            salida += episodio
            return salida, 200
        else:
            return "Ha ocurrido algún error en la modificación", 400

@app.route('/episodio', methods=['DELETE'])
def elimina_episodio():
    params = request.get_json()
    if params == None:
        return "Error: No se ha encontrado fichero de entrada", 400
    elif 'eliminar' not in params:
        return "Error: Formato incorrecto", 400 
    elif 'id' not in params['eliminar']:
        return "Error: No se ha especificado el id del episodio a eliminar", 400
    else:
        id_episodio = params['eliminar']['id']
        db = DatabaseMongoDB()
        result = json.loads(db.elimina_episodio(id_episodio))
        if(result['ok'] == 1.0):
            salida = "Se ha eliminado el episodio de id " + str(id_episodio)
        return salida, 200