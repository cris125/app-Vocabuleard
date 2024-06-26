import mysql.connector
import variableGlobal
class CrearTablas():
    conexion = variableGlobal.baseDatosConeccion
    
    def __init__(self) -> None:
        self.create_table_prueba()
        self.create_table_usuario()
        self.create_table_account()
        
    def create_table_prueba(self):
        try:
            cursor = self.conexion.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pruebas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre TEXT,
                    preguntas TEXT,
                    intentos INT,
                    calificacion INT
                )
            ''')
            self.conexion.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print("Error al guardar en la base de datos:", e)
            
            
    def create_table_usuario(self):
        try:
            cursor = self.conexion.cursor()

            # Define la estructura de la tabla
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    userName VARCHAR(255),
                    contrasena VARCHAR(255),
                    id_Account INT,
                    promNota VARCHAR(255)
                )
            ''')
            self.conexion.commit()
        except mysql.connector.Error as e:
            print("Error al crear la tabla de usuarios:", e)
        finally:
            if cursor:
                cursor.close()
                
    def create_table_account(self):
        try:
            cursor = self.conexion.cursor()
            
            # Define la estructura de la tabla
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS account (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    prueba VARCHAR(255),
                    activate BOOLEAN,
                    admin BOOLEAN            
                )
            ''')
            self.conexion.commit()
        except mysql.connector.Error as e:
            print("Error al crear la tabla de cuentas:", e)
        finally:
            if cursor:
                cursor.close()
                
    def get_last_id_usuario(self):
        last_id = 0
        try:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT MAX(id) FROM usuarios')
            last_id = cursor.fetchone()[0]
        except mysql.connector.Error as e:
            print("Error al obtener el último ID de usuario:", e)
        finally:
            if cursor:
                cursor.close()
        return last_id
    
    def get_last_id_account(self):
        last_id = 0
        try:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT MAX(id) FROM account')
            last_id = cursor.fetchone()[0]
        except mysql.connector.Error as e:
            print("Error al obtener el último ID de cuenta:", e)
        finally:
            if cursor:
                cursor.close()
        return last_id
