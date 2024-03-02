
import sqlite3

from Account import Account  # Asumiendo que la clase Account está en un archivo llamado Account.py

class Usuario():
    
    
    def __init__(self, userName: str):
        self.id = None
        self.account = Account()
        self.userName = userName

    def __str__(self) -> str:
        return str(self.userName)

# Función para crear la tabla en la base de datos

    
def get_last_id():
    connection = sqlite3.connect('sql3.db')
    cursor = connection.cursor()

    cursor.execute('SELECT MAX(id) FROM usuarios')
    last_id = cursor.fetchone()[0]

    connection.close()

    return last_id if last_id is not None else 0

# Función para insertar un usuario en la base de datos
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
        
def create_table2():
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        
        # Define la estructura de la tabla
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS uasas (
                id INTEGER PRIMARY KEY,
                userNaasdsae TEXT
            )
            
        ''')
        connection.commit()
        connection.close()        
def insert_usuario(usuario):
    last_id = get_last_id()
    usuario.id = last_id + 1
    
    connection = sqlite3.connect('sql3.db')
    cursor = connection.cursor()
    
    # Inserta el usuario en la tabla
    cursor.execute('''
        INSERT INTO usuarios (id, userName)
        VALUES (?, ?)
    ''', (usuario.id, usuario.userName))

    connection.commit()
    connection.close()

# Ejemplo de uso
create_table()
create_table2()
usuario1 = Usuario("John Doe")
# Aquí puedes realizar operaciones en la cuenta del usuario si es necesario
insert_usuario(usuario1)