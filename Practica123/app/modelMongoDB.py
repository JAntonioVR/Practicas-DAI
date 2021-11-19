from pymongo import MongoClient
from bson.json_util import dumps

class DatabaseMongoDB:
    def __init__(self):  
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
        self.episodios = self.db.samples_friends
    
    def busca_episodios_nombre(self, nombre):

        lista_episodios = []

        episodios_buscados = self.episodios.find(
            { 'name': {'$regex': nombre } }
        )

        for episodio in episodios_buscados:
            lista_episodios.append(dumps(episodio))
        return lista_episodios

    def anade_episodio(self, episodio):
        return dumps(self.episodios.insert(episodio))

    def modifica_episodio(self, episodio):
        result = self.episodios.update(
            { 'id': episodio['id'] },
            {'$set': episodio}
        )
        return dumps(result)

    def elimina_episodio(self, id_episodio):
        return dumps(self.episodios.deleteOne())