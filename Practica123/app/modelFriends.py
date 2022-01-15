# ./app/modelFriends.py
#
# ────────────────────────────────────────────────────────────────────────────────
#   :::::: modelFriends.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────
#
# Práctica 2 de DAI: Bases de Datos NoSQL, API RESTFULL
# Autor: Juan Antonio Villegas Recio
# Curso 2021-2022
# Universidad de Granada

# Fichero que emula el MODELO de una aplicación web, encapsulando el código
# de la base de datos de capítulos de Friends.

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from pymongo import MongoClient

#
# ────────────────────────────────────────────────────────────────────────────────────────────
#   :::::: CLASE   DatabaseFriends : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────────────────
#
# Clase que encapsula la interacción con la base de datos de MongoDB

class DatabaseFriends:

    # ─── INICIALIZADOR ──────────────────────────────────────────────────────────────
    def __init__(self):  
        client = MongoClient("mongo", 27017)        # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections          # Elegimos la base de datos de ejemplo
        self.episodios = self.db.samples_friends    # Para tener a mano la coleccion de episodios de FRIENDS


    # ─── BUSQUEDA DE EPISODIOS POR TEMPORADA ────────────────────────────────────────
    # Busca los episodios de la temporada especificada como argumento y los devuelve
    # en un array.
    def busca_episodios_temporada(self, temporada):
        lista_episodios = []
        episodios_buscados = self.episodios.find(
            {"season": temporada}
        )
        for episodio in episodios_buscados:
            lista_episodios.append(episodio)
        return lista_episodios

    # ────────────────────────────────────────────────────────────────────────────────
    # ─── METODOS RESPECTIVOS A LA APIREST ───────────────────────────────────────────
    # ────────────────────────────────────────────────────────────────────────────────

    # ─── PRIMER ID DISPONIBLE ───────────────────────────────────────────────────────
    # Recorre los IDs de los registros de la BD y devuelve un entero disponible para
    # ser asignado como ID a un nuevo capítulo.
    def __buscar_primer_id_disponible__(self):
        mayor_id = 0
        for episodio in self.episodios.find():
            if 'id' in episodio:
                if episodio['id'] > mayor_id:
                    mayor_id = episodio['id']
        return mayor_id + 1


    # ─── BUSQUEDA DE EPISODIOS POR ID ───────────────────────────────────────────────
    # Busca un episodio a partir de su identificador y devuelve el episodio en formato
    # json si lo encuentra o None en caso contrario
    def busca_episodio_id(self, id):
        episodios_buscados = self.episodios.find(
            { 'id': id }
        )
        episodios = []
        for episodio in episodios_buscados:
            episodios.append(episodio)

        if(len(episodios) > 0):
            return episodios[0]
        else:
            return None

    # ─── BUSQUEDA DE EPISODIOS POR NOMBRE Y SINOPSIS ────────────────────────────────
    # Busca los episodios de la BD que contienen 'nombre' en su atributo 'name' y 
    # 'sinopsis' en su atributo 'summary'.
    # Devuelve un array de episodios en formato json, posiblemente vacío si la
    # busqueda no devuelve ningun resultado.
    def busca_episodios_nombre_sinopsis(self, nombre, sinopsis):

        lista_episodios = []
        episodios_buscados = self.episodios.find( {
            '$and': [
                { 'name': {'$regex': nombre } },
                { 'summary': {'$regex': sinopsis } }
            ]
            
        } )

        for episodio in episodios_buscados:
            episodio['_id'] = ""
            lista_episodios.append(episodio)

        return lista_episodios

    # ─── AÑADIR EPISODIO ────────────────────────────────────────────────────────────
    # Inserta un nuevo documento en la colección de episodios. Los campos y los
    # valores del nuevo episodio se encuentran en el diccionario 'episodio'.
    # Devuelve el campo '_id' del nuevo episodio.
    def anade_episodio(self, episodio):
        episodio['id'] = self.__buscar_primer_id_disponible__()
        return self.episodios.insert(episodio)


    # ─── MODIFICAR EPISODIO ─────────────────────────────────────────────────────────
    # Modifica un episodio existente. El diccionario 'episodio' contiene el 'id' del
    # episodio a modificar junto con los valores de los campos a modificar.
    # Devuelve el objeto json con el episodio modificado en caso de exito o None
    # si no se ha completado la modificación
    def modifica_episodio(self, episodio):

        result = self.episodios.update(
            { 'id': episodio['id'] },
            {'$set': episodio}
        )
        # print(result, flush=True)
        if result['updatedExisting']:
            episodio = self.busca_episodio_id(episodio['id'])
            print(episodio, flush=True)
            return episodio
        else:
            return None


    # ─── ELIMINAR EPISODIO ──────────────────────────────────────────────────────────
    # Elimina el documento cuyo atributo 'id' viene dado como argumento.
    # Devuelve True si se ha completado correctamente el borrado y False en otro caso.
    def elimina_episodio(self, id_episodio):
        result = self.episodios.remove({ 'id': id_episodio })
        if result['n'] > 0:
            return True
        else:
            return False

# ────────────────────────────────────────────────────────────────────────────────
