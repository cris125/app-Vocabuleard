import mysql.connector
from models.usuario import Usuario
from baseDeDatos.crearTablas import CrearTablas
import variableGlobal
class DbUsuario:
    crearTablas = CrearTablas()
    
    conexion = variableGlobal.baseDatosConeccion
    
    def crearAdmin(self, user: str,contrasena:str):
        try:
            if not self.verificar_usuario(user):
                newAdmin = Usuario(user,contrasena)
                newAdmin.account.admin=True
                self.insert_usuario(newAdmin)
                return(user)
            else:
                print("El admin ya existe")
                return(user)
        except mysql.connector.Error as e:
            print(f"Error al crear admin: {e}")
            
    def crearUsuario(self, user: str,contrasena:str):
        try:
            if not self.verificar_usuario(user):
                newUser = Usuario(user,contrasena)
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
                return (usuario[0][0],usuario[0][1],self.getAccountId(usuario[0][2]),usuario[0][3])
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


    def insert_usuario(self, usuario:Usuario):
        try:
            self.insert_account(usuario)
            cursor = self.conexion.cursor()
            cursor.execute('''
                INSERT INTO usuarios (id, userName, contrasena, id_account, promNota)
                VALUES (%s,%s ,%s, %s, %s)
            ''', (usuario.id, usuario.userName, usuario.contrasena, usuario.id_account, usuario.promNota))
            self.conexion.commit()
            print("Usuario insertado correctamente.")
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

    def modify_promNota(self, usuario_id, new_promNota):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                UPDATE usuarios
                SET promNota = %s
                WHERE id = %s
            ''', (new_promNota, usuario_id))
            self.conexion.commit()
            print(f"El valor de promNota para el usuario con ID {usuario_id} se ha modificado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al modificar promNota: {e}")
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
                
    def actualizar_prueba(self, usuario_id: int, nuevo_valor_prueba: str):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                UPDATE account 
                SET prueba = %s
                WHERE id = (
                    SELECT id_account FROM usuarios WHERE id = %s
                )
            ''', (nuevo_valor_prueba, usuario_id))
            self.conexion.commit()
        except mysql.connector.Error as e:
            print(f"Error al modificar prueba: {e}")
        finally:
            if cursor:
                cursor.close()



    

