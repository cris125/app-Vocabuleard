
import sqlite3
class CrearTablas():
    coneccion='sql3.db'
    def create_table_usuario(self):
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
            connection.close()
            
    def create_table_account(self):
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
            connection.close()   
            
    def get_last_id_usuario(self):
        self.create_table_usuario()
        connection = sqlite3.connect(self.coneccion)
        cursor = connection.cursor()
        cursor.execute('SELECT MAX(id) FROM usuarios')
        last_id = cursor.fetchone()[0]
        connection.close()
        return last_id if last_id is not None else 0


    def get_last_id_account(self):
        self.create_table_account()
        connection = sqlite3.connect(self.coneccion)
        cursor = connection.cursor()
        cursor.execute('SELECT MAX(id) FROM account')
        last_id = cursor.fetchone()[0]
        connection.close()
        return last_id if last_id is not None else 0