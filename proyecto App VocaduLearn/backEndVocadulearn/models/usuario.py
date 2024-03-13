
import sqlite3

from models.account import Account  # Asumiendo que la clase Account está en un archivo llamado Account.py
from views.crearTablas import CrearTablas
class Usuario():
    
    def __init__(self, userName: str):
        crearTablas=CrearTablas()
        self.id=int(crearTablas.get_last_id_usuario())+1
        self.account=Account()
        self.id_account = self.account.id
        self.userName = userName

    def __str__(self) -> str:
        return str(self.userName)

