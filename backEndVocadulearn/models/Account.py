from ..viws.utilsSql import crearTablas
class Account:
    def __init__(self):
        last_id = crearTablas.get_last_id_usuario()
        self.id = last_id + 1
        self.prueba= None
        self.activate=True
        self.nota=None