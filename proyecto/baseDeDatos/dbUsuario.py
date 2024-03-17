import mysql.connector
from models.usuario import Usuario
from baseDeDatos.crearTablas import CrearTablas

class DbUsuario:
    crearTablas = CrearTablas()
    conexion = mysql.connector.connect(
        host="monorail.proxy.rlwy.net",
        user="root",
        password="VQkGgBYZGwDkSDSoDNBUDKooRxdwJUOJ",
        port="16333",
        database="railway"
    )

    def crearUsuario(self, user: str):
        try:
            if not self.verificar_usuario(user):
                self.crearTablas.create_table_account()
                self.crearTablas.create_table_usuario()
                newUser = Usuario(user)
                self.insert_usuario(newUser)
            else:
                print("El usuario ya existe")
        except mysql.connector.Error as e:
            print(f"Error al crear usuario: {e}")

    def insert_usuario(self, usuario):
        try:
            self.insert_account(usuario)
            cursor = self.conexion.cursor()
            cursor.execute('''
                INSERT INTO usuarios (id, userName, id_account)
                VALUES (%s, %s, %s)
            ''', (usuario.id, usuario.userName, usuario.id_account))
            self.conexion.commit()
        except mysql.connector.Error as e:
            print(f"Error al insertar usuario: {e}")
        finally:
            if cursor:
                cursor.close()

    def insert_account(self, usuario: Usuario):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                INSERT INTO account (
                    id, 
                    prueba,
                    activate)
                VALUES (%s, %s, %s)
            ''', (usuario.id_account, usuario.account.prueba, usuario.account.activate))
            self.conexion.commit()
        except mysql.connector.Error as e:
            print(f"Error al insertar cuenta: {e}")
        finally:
            if cursor:
                cursor.close()

    def ver_tabla_usuario(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT * FROM usuarios;
            ''')
            usuarios = cursor.fetchall()
            return usuarios
        except mysql.connector.Error as e:
            print(f"Error al ver tabla de usuarios: {e}")
        finally:
            if cursor:
                cursor.close()

    def ver_tabla_account(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT * FROM account WHERE id = %s;
            ''', (id,))
            usuarios = cursor.fetchall()
            return usuarios
        except mysql.connector.Error as e:
            print(f"Error al ver tabla de cuentas: {e}")
        finally:
            if cursor:
                cursor.close()

    def ver_account(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT * FROM account;
            ''')
            usuarios = cursor.fetchall()
            return usuarios
        except mysql.connector.Error as e:
            print(f"Error al ver cuentas: {e}")
        finally:
            if cursor:
                cursor.close()

    def verificar_usuario(self, nombre_usuario):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE userName = %s", (nombre_usuario,))
            resultado = cursor.fetchone()
            return resultado[0] > 0
        except mysql.connector.Error as e:
            print(f"Error al verificar usuario: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

# Ejemplo de uso

    
