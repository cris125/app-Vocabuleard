from views.crearTablas import CrearTablas

class Account:
    def __init__(self):
        crearTablas=CrearTablas()
        last_id = crearTablas.get_last_id_account()# Usar el método correcto para obtener el último ID de cuenta
        self.id = last_id +1
        self.prueba = None
        self.activate = True
        self.nota = None
