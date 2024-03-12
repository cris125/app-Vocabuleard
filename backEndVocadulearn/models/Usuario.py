
import sqlite3

from Account import Account  # Asumiendo que la clase Account está en un archivo llamado Account.py
from viws import crearTablas

class Usuario():
    
    def __init__(self, userName: str):
        last_id = crearTablas.get_last_id_usuario()
        self.id = last_id + 1
        self.account=Account()
        self.id_account = self.account.id
        self.userName = userName

    def __str__(self) -> str:
        return str(self.userName)

