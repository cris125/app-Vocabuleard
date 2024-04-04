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
    def crearAdmin(self, user: str):
        try:
            if not self.verificar_usuario(user):
                newAdmin = Usuario(user)
                newAdmin.account.admin=True
                self.insert_usuario(newAdmin)
                return(user)
            else:
                print("El admin ya existe")
                return(user)
        except mysql.connector.Error as e:
            print(f"Error al crear admin: {e}")
            
    def crearUsuario(self, user: str):
        try:
            if not self.verificar_usuario(user):
                newUser = Usuario(user)
                self.insert_usuario(newUser)
                return(self.getUser(user))
            else:
                print("El usuario ya existe")
                return(self.getUser(user))
        except mysql.connector.Error as e:
            print(f"Error al crear usuario: {e}")

    def getUser(self, usuarioStr):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT * FROM usuarios WHERE userName = %s 
            ''', (usuarioStr,))
            usuario = cursor.fetchall()
            if len(usuario)>0 :
                return (usuario[0][0],usuario[0][1],self.getAccountId(usuario[0][2]))
            else:
                return(None)
        except mysql.connector.Error as e:
            print(f"Error al ver tabla de usuarios: {e}")
        finally:
            if cursor:
                cursor.close()
    
    
    def getAccountId(self, id:int):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT * FROM account WHERE id = %s 
            ''', (id,))
            account = cursor.fetchall()
            return account
        except mysql.connector.Error as e:
            print(f"Error al ver tabla de account: {e}")
        finally:
            if cursor:
                cursor.close()


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
                    activate,
                    admin)
                VALUES (%s, %s, %s, %s)
            ''', (usuario.id_account, usuario.account.prueba, usuario.account.activate,usuario.account.admin))
            self.conexion.commit()
        except mysql.connector.Error as e:
            print(f"Error al insertar cuenta: {e}")
        finally:
            if cursor:
                cursor.close()
                
    def eliminar_usuario(self, idUsuario, idAccount):
        try:
            self.eliminar_account(idAccount)
            cursor = self.conexion.cursor()
            cursor.execute('''
                DELETE FROM usuarios WHERE id = %s
            ''', (idUsuario,))
            self.conexion.commit()
        except mysql.connector.Error as e:
            print(f"Error al eliminar usuario: {e}")
        finally:
            if cursor:
                cursor.close()

    def eliminar_account(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                DELETE FROM account WHERE id = %s
            ''', (id,))
            self.conexion.commit()
        except mysql.connector.Error as e:
            print(f"Error al eliminar cuenta: {e}")
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

    

