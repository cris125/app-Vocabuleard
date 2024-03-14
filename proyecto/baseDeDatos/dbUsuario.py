import sqlite3
from models.usuario import Usuario
from baseDeDatos.crearTablas import CrearTablas

class DbUsuario:
    crearTablas = CrearTablas()
    coneccion = 'sql3.db'

    def crearUsuario(self, user: str):
        try:
            if not self.verificar_usuario(user):
                self.crearTablas.create_table_account()
                self.crearTablas.create_table_usuario()
                newUser = Usuario(user)
                self.insert_usuario(newUser)
            else:
                print("El usuario ya existe")
        except sqlite3.Error as e:
            print(f"Error al crear usuario: {e}")

    def insert_usuario(self, usuario):
        try:
            self.insert_account(usuario)
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO usuarios (id, userName, id_account)
                VALUES (?, ?, ?)
            ''', (usuario.id, usuario.userName, usuario.id_account))
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error al insertar usuario: {e}")
        finally:
            if connection:
                connection.close()

    def insert_account(self, usuario: Usuario):
        try:
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO account (
                    id, 
                    prueba,
                    activate)
                VALUES (?, ?, ?)
            ''', (usuario.id_account, usuario.account.prueba, usuario.account.activate))
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error al insertar cuenta: {e}")
        finally:
            if connection:
                connection.close()

    def ver_tabla_usuario(self):
        try:
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM usuarios;
            ''')
            usuarios = cursor.fetchall()
            return usuarios
        except sqlite3.Error as e:
            print(f"Error al ver tabla de usuarios: {e}")
        finally:
            if connection:
                connection.close()

    def ver_tabla_account(self, id):
        try:
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM account WHERE id = ?;
            ''', (id,))
            usuarios = cursor.fetchall()
            return usuarios
        except sqlite3.Error as e:
            print(f"Error al ver tabla de cuentas: {e}")
        finally:
            if connection:
                connection.close()

    def ver_account(self):
        try:
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM account;
            ''')
            usuarios = cursor.fetchall()
            return usuarios
        except sqlite3.Error as e:
            print(f"Error al ver cuentas: {e}")
        finally:
            if connection:
                connection.close()

    def verificar_usuario(self, nombre_usuario):
        try:
            conexion = sqlite3.connect(self.coneccion)
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE userName = ?", (nombre_usuario,))
            resultado = cursor.fetchone()
            return resultado[0] > 0
        except sqlite3.Error as e:
            print(f"Error al verificar usuario: {e}")
            return False
        finally:
            if conexion:
                conexion.close()

# Ejemplo de uso


    

