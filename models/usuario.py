
from models.account import Account
from baseDeDatos.crearTablas import CrearTablas

class Usuario():
    
    def __init__(self, userName: str):
        crearTablas = CrearTablas()
        last_id = crearTablas.get_last_id_usuario()
        if last_id is None:
            self.id = 1  # Si no hay usuarios, establecer el ID como 1
        else:
            self.id = int(last_id) + 1
        self.account = Account()
        self.id_account = self.account.id
        self.userName = userName
        self.promNota= None
    def __str__(self) -> str:
        return str(self.userName)

