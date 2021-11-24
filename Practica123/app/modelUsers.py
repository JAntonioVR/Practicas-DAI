# ./app/model.py
#
# ────────────────────────────────────────────────────────────────
#   :::::: model.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────
#
# Práctica 2 de DAI: Plantillas, Manejo de Sesiones y Frameworks CSS
# Autor: Juan Antonio Villegas Recio
# Curso 2021-2022
# Universidad de Granada

# Fichero que emula el MODELO de una aplicación web, encapsulando el código
# de la base de datos

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from pickleshare import *
import hashlib

#
# ──────────────────────────────────────────────────────────────────────────────
#   :::::: C L A S E   D A T A B A S E : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────
# Clase que encapsula la interacción con la BD de pickleshare

class DatabaseUsers:

    # ─── INICIALIZADOR ──────────────────────────────────────────────────────────────
    def __init__(self):
        self.db = PickleShareDB('./database') # En './database' se almacena el contenido de la BD

    # ─── AÑADIR USUARIO ─────────────────────────────────────────────────────────────
    # Añade un usuario nuevo a la base de datos. El email y el teléfono son opcionales
    def anadir_usuario(self, username, passwd, name, email=None, phone=None):
        self.db[username] = {
                        "username" : username,
                        "password" : self.hash_passwd(passwd),
                        "name"     : name,
                        "email"    : email,
                        "phone"    : phone
                    }

    # ─── MODIFICAR USUARIO ──────────────────────────────────────────────────────────
    # Modifica los usuarios de un usuario dado su 'username'. Se asume que no se
    # puede modificar ni el nombre de usuario ni su contraseña. Devuelve el objeto
    # usuario ya modificado o None si no encuentra el usuario a modificar.
    def modificar_usuario(self, username, new_name, new_email, new_phone):
        if(username in self.db):
            self.db[username]["name"] = new_name
            self.db[username]["email"] = new_email
            self.db[username]["phone"] = new_phone
            self.db[username] = self.db[username]
            return self.db[username]
        else:
            return None

    # ─── BÚSQUEDA DE USUARIO ────────────────────────────────────────────────────────
    # Busca y devuelve un usuario a partir de su nombre de usuario. Devuelve None si
    # este usuario no se encuentra en la BD.
    def buscar_usuario(self, username):
        if(username in self.db):
            return self.db[username]
        else:
            return None
        
    # ─── COMPROBACION DE LOGIN ──────────────────────────────────────────────────────
    # Dados un nombre de usuario y su contraseña, comprueba si el usuario se 
    # corresponde con la contraseña.
    def comprobar_login(self, username, passwd):
        if(username in self.db):
            return self.db[username]['password'] == self.hash_passwd(passwd)
        else:
            return False

    # ─── HASH ───────────────────────────────────────────────────────────────────────
    # Codifica una contraseña
    @staticmethod
    def hash_passwd(passwd):
        return(hashlib.sha224(passwd.encode('utf-8')).hexdigest())