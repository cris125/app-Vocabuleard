import sqlite3

from models import Usuario
from viws.utilsSql import crearTablas
class viwUsuario:
    def crearUsuario(self,user:str):
        crearTablas.create_table_account()
        crearTablas.create_table_usuario()
        newUser=Usuario(user)
        self.insert_usuario(newUser)

    def insert_usuario(self,usuario):
        
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO usuarios (id, userName,id_account)
            VALUES (?, ?, ?)
        ''', (usuario.id, usuario.userName,usuario.id_account))
        connection.commit()
        connection.close()

    def insert_account(self,usuario:Usuario):
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO account (
                id, 
                prueba,
                activate)
            VALUES (?, ?,?)
        ''', (usuario.id_account, usuario.account.prueba,usuario.account.activate))
        connection.commit()
        connection.close()
            
    def ver_tabla(self):
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        # Define la estructura de la tabla
        cursor.execute('''
            SELECT * FROM  usuarios; 
        ''')
        usuarios = cursor.fetchall()
        connection.close()
        return(usuarios)
# Ejemplo de uso
crearUsuario("John Doe")
ver_tabla()

