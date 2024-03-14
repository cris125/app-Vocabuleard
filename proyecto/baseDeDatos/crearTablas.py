
import sqlite3

class CrearTablas():
    coneccion = 'sql3.db'
    
    def create_table_usuario(self):
        try:
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            
            # Define la estructura de la tabla
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    userName TEXT,
                    id_Account INTEGER
                )
            ''')
            connection.commit()
        except sqlite3.Error as e:
            print("Error al crear la tabla de usuarios:", e)
        finally:
            if connection:
                connection.close()
                
    def create_table_account(self):
        try:
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            
            # Define la estructura de la tabla
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS account (
                    id INTEGER PRIMARY KEY,
                    prueba TEXT,
                    activate BOOLEAN           
                )
            ''')
            connection.commit()
        except sqlite3.Error as e:
            print("Error al crear la tabla de cuentas:", e)
        finally:
            if connection:
                connection.close()
                
    def get_last_id_usuario(self):
        last_id = 0
        try:
            self.create_table_usuario()
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            cursor.execute('SELECT MAX(id) FROM usuarios')
            last_id = cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("Error al obtener el último ID de usuario:", e)
        finally:
            if connection:
                connection.close()
        return last_id
    
    def get_last_id_account(self):
        last_id = 0
        try:
            self.create_table_account()
            connection = sqlite3.connect(self.coneccion)
            cursor = connection.cursor()
            cursor.execute('SELECT MAX(id) FROM account')
            last_id = cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("Error al obtener el último ID de cuenta:", e)
        finally:
            if connection:
                connection.close()
        return last_id
