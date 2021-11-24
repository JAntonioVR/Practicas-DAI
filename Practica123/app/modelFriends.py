from pymongo import MongoClient
from bson.json_util import dumps

class DatabaseFriends:
    def __init__(self):  
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
        self.episodios = self.db.samples_friends

    def __buscar_primer_id_disponible__(self):
        mayor_id = 0
        salida = ""

        for episodio in self.episodios.find():
            if 'id' in episodio:
                if episodio['id'] > mayor_id:
                    mayor_id = episodio['id']
        return mayor_id + 1

    def busca_episodio_id(self, id):
        episodios_buscados = self.episodios.find(
            { 'id': id }
        )
        episodios = []
        for episodio in episodios_buscados:
            episodios.append(dumps(episodio))

        if(len(episodios) > 0):
            return episodios
        else:
            return None


    def busca_episodios_nombre(self, nombre):

        lista_episodios = []

        episodios_buscados = self.episodios.find(
            { 'name': {'$regex': nombre } }
        )

        for episodio in episodios_buscados:
            lista_episodios.append(dumps(episodio))
        if len(lista_episodios) > 0:
            return lista_episodios, 200
        else:
            return "No se ha encontrado ningún episodio", 200

    def busca_episodios_temporada(self, temporada):
        lista_episodios = []
        episodios_buscados = self.episodios.find(
            {"season": temporada}
        )
        for episodio in episodios_buscados:
            lista_episodios.append(episodio)
        return lista_episodios

    def anade_episodio(self, episodio):
        episodio['id'] = self.__buscar_primer_id_disponible__()
        return dumps(self.episodios.insert(episodio))

    def modifica_episodio(self, episodio):
        result = self.episodios.update(
            { 'id': episodio['id'] },
            {'$set': episodio}
        )
        return dumps(result)

    def elimina_episodio(self, id_episodio):
        return dumps(self.episodios.remove({ 'id': id_episodio }))