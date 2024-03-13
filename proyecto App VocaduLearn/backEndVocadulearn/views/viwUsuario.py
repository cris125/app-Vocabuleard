import sqlite3

from models.usuario import Usuario
from views.crearTablas import CrearTablas


class ViwUsuario:
    crearTablas=CrearTablas()
    coneccion='sql3.db'
    def crearUsuario(self,user:str):
        if not self.verificar_usuario(user):
            
            self.crearTablas.create_table_account()
            self.crearTablas.create_table_usuario()
            newUser=Usuario(user)
            self.insert_usuario(newUser)
        else:
            print("ya exsite")

    def insert_usuario(self,usuario):
        self.insert_account(usuario)
        connection = sqlite3.connect(self.coneccion)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO usuarios (id, userName,id_account)
            VALUES (?, ?, ?)
        ''', (usuario.id, usuario.userName,usuario.id_account))
        connection.commit()
        connection.close()

    def insert_account(self,usuario:Usuario):
        connection = sqlite3.connect(self.coneccion)
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
            
    def ver_tabla_usuario(self):
        connection = sqlite3.connect(self.coneccion)
        cursor = connection.cursor()
        # Define la estructura de la tabla
        cursor.execute('''
            SELECT * FROM  usuarios; 
        ''')
        usuarios = cursor.fetchall()
        connection.close()
        return(usuarios)
    
    def ver_tabla_account(self,id):
        connection = sqlite3.connect(self.coneccion)
        cursor = connection.cursor()
        # Define la estructura de la tabla
        cursor.execute('''
            SELECT * FROM  account WHERE id = ?; 
        ''',(id,))
        usuarios = cursor.fetchall()
        connection.close()
        return(usuarios)
    
    def ver_account(self):
        connection = sqlite3.connect(self.coneccion)
        cursor = connection.cursor()
        # Define la estructura de la tabla
        cursor.execute('''
            SELECT * FROM  account; 
        ''')
        usuarios = cursor.fetchall()
        connection.close()
        return(usuarios)
    
    def verificar_usuario(self,nombre_usuario):
        try:
            conexion = sqlite3.connect(self.coneccion)
            cursor = conexion.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE userName = ?", (nombre_usuario,))
            resultado = cursor.fetchone()

            # Comprobar si el resultado es mayor que cero (usuario existe) o igual a cero (usuario no existe)
            if resultado[0] > 0:
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"Error al verificar el usuario: {e}")
            return False
        finally:
            conexion.close()
# Ejemplo de uso

    

