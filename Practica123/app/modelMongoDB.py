from pymongo import MongoClient
from bson.json_util import dumps

class DatabaseMongoDB:
    def __init__(self):  
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
        self.episodios = self.db.samples_friends

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

    def anade_episodio(self, episodio):
        return dumps(self.episodios.insert(episodio))

    def modifica_episodio(self, episodio):
        result = self.episodios.update(
            { 'id': episodio['id'] },
            {'$set': episodio}
        )
        return dumps(result)

    def elimina_episodio(self, id_episodio):
        return dumps(self.episodios.remove({ 'id': id_episodio }))