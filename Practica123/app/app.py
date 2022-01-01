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

from modelUsers import DatabaseUsers
from modelFriends import DatabaseFriends
from flask import Flask, render_template, flash, render_template, request, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



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

# NOTE: A partir del ejercicio 4 no se han implementado enlaces en el menú desplegable
# de la web de la práctica 2.

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
    patron = "\w+@\w+\.(com|es)"
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
def index():
    return render_template('index.html')


# ─── LOG IN ──────────────────────────────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    status = 0
    db = DatabaseUsers()
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
    db = DatabaseUsers()
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
    db = DatabaseUsers()
    if('username' in session and session['username'] != None):
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
    db = DatabaseUsers()
    if 'username' in session and session['username'] != None:
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


#
# ──────────────────────────────────────────────────────────── I ──────────
#   :::::: P R A C T I C A   3 : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────
#

temporadas = ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', 'Season 6', 'Season 7', 'Season 8', 'Season 9', 'Season 10' ]

# ─── CONSULTA Y VISUALIZACION DE CAPITULOS ──────────────────────────────────────
def ver_capitulos_temporada(temporada):
    status = 0
    lista_episodios = []
    db = DatabaseFriends()
    lista_episodios = db.busca_episodios_temporada(temporada)
    if len(lista_episodios) > 0:
        status = 1
    return render_template('lista.html', status = status, episodios = lista_episodios, temporadas = temporadas, temporada_buscada = temporada)

# ─── BUSQUEDA DE CAPITULOS POR TEMPORADA ────────────────────────────────────────
# Ahora la página de los capítulos será la página principal
@app.route("/")
@app.route('/index')
@app.route("/busca_coleccion/<int:temporada>")
@app.route("/busca_coleccion", methods=['GET', 'POST'])
def busca_coleccion(temporada=0):
    if(temporada == 0):
        if request.method == 'POST':
            temporada = int(request.form['temporada'].split()[1])
        else:
            temporada = 1

    if(temporada < 1 or temporada > 10):
        temporada = 1
    
    return ver_capitulos_temporada(temporada)

#
# ──────────────────────────────────────────────────────────────── II ──────────
#   :::::: A P I   R E S T F U L L : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────
#


# ─── BUSCAR EPISODIO POR NOMBRE Y SINOPSIS ──────────────────────────────────────
# En el campo 'busqueda' debe haber un campo 'nombre' o un campo 'sinopsis'. 
# Se buscarán episodios que contengan la subcadena 'nombre' en el nombre del 
# episodio y la subcadena 'sinopsis' en la sinopsis. Si alguno de los dos campos
# no se especifica se busca solo en base al otro.
# Devuelve todos los episodios encontrados en formato json.
@app.route('/episodio', methods=['GET'])
def busca_episodio():

    params = request.get_json(force=True)

    if params == None:
        return "Error: No se ha encontrado fichero de entrada", 400
    elif 'nombre' not in params and 'sinopsis' not in params:
        return "Error: No se ha especificado ningún criterio a buscar", 400
    else:
        nombre, sinopsis = "", ""
        if 'nombre' in params:
            nombre = params['nombre']
        if 'sinopsis' in params:
            sinopsis = params['sinopsis']

        db = DatabaseFriends()
        episodios = db.busca_episodios_nombre_sinopsis(nombre, sinopsis)
        if len(episodios) > 0:
            return "\n".join([str(episodio) for episodio in episodios]), 200
        else:
            return "No se ha encontrado ningún episodio.", 200

# FIXME
# ─── INSERTAR EPISODIO NUEVO ────────────────────────────────────────────────────
# En el campo 'anadir' debe haber un diccionario con varios pares clave-valor que
# serán los campos que tendrá el nuevo episodio que se añada. Se aceptan los 
# atributos 'url', 'name', 'season', 'number', 'airdate', 'airtime', 'airstamp',
# 'runtime', 'image' y 'summary', aunque todos ellos salvo 'name' son opcionales.
# Se añade a la BD y se devuelve un objeto json con el campo '_id' de tipo
# ObjectID con el que se almacena en la BD. No es necesario especificar el campo
# 'id' porque al insertar el capítulo se genera automáticamente un identificador
# entero único para el nuevo episodio.
@app.route('/episodio', methods=['POST'])
def anade_episodio():
    params = request.get_json(force=True)
    if params == None:
        return "Error: No se ha encontrado entrada", 200
    elif 'name' not in params:
        return "Error: Es obligatorio especificar el episodio", 200 
    else:
        args = params
        db = DatabaseFriends()
        salida = db.anade_episodio(args)
        salida = "Se ha añadido un nuevo episodio:  " + str(salida)
        return salida, 200


# ─── MODIFICAR EPISODIO ─────────────────────────────────────────────────────────
# En el campo 'modificar' debe haber un diccionario con varios pares clave-valor 
# que serán los nuevos valores del episodio. En este caso se requiere también un
# par clave valor para el atributo 'id', para así referenciar qué capítulo se
# desea modificar. El episodio referenciado se modifica si existe y se devuelve
# un mensaje de éxito o error, acompañado de un objeto json con los nuevos valores
# del episodio modificado en caso de éxito.
@app.route('/episodio', methods=['PUT'])
def modifica_episodio():
    params = request.get_json(force=True)
    if params == None:
        return "Error: No se ha encontrado fichero de entrada", 400
    elif 'id' not in params:
        return "Error: No se ha especificado el id del episodio a modificar", 400
    else:
        id_episodio = int(params['id'])
        args = params

        # Modificamos el documento con los nuevos datos
        db = DatabaseFriends()
        result = db.modifica_episodio(args)

        # Comprobamos que todo haya ido bien
        if result != None:
            salida = "Se ha modificado el episodio de id " + str(id_episodio) + "  " + str(result)
            return salida, 200
        else:
            return "Ha ocurrido algún error en la modificación, ¿existe un capítulo con id " + str(id_episodio) + "?", 400


# ─── BORRAR EPISODIO ────────────────────────────────────────────────────────────
# En el campo 'eliminar' debe haber un diccionario con un único par clave-valor,
# el correspondiente al identificador único del episodio que se desea eliminar, 
# 'id'. Se elimina el episodio referenciado si existe y se muestra como salida
# un mensaje de éxito o error.
@app.route('/episodio', methods=['DELETE'])
def elimina_episodio():
    params = request.get_json()
    if params == None:
        return "Error: No se ha encontrado fichero de entrada", 400
    elif 'id' not in params:
        return "Error: No se ha especificado el id del episodio a eliminar", 400
    else:
        id_episodio = params['id']
        db = DatabaseFriends()
        result = db.elimina_episodio(id_episodio)
        if(result):
            salida = "Se ha eliminado el episodio de id " + str(id_episodio)
            return salida, 200
        else:
            return "Ha ocurrido algún error en la eliminación, ¿existe un capítulo con id " + str(id_episodio) + "?", 400

# ────────────────────────────────────────────────────────────────────────────────


@app.route('/formulario_modificar/<int:id>')
def formulario_modificar(id):
    db = DatabaseFriends()
    episodio = db.busca_episodio_id(id)
    return render_template('modify_episode.html', id = id, episodio = episodio)