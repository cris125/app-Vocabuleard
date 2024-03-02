import sqlite3
class BaseDatos():
    def create_table():
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        
        # Define la estructura de la tabla
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                userName TEXT
            )
        ''')
        connection.commit()
        connection.close()