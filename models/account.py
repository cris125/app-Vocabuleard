from baseDeDatos.crearTablas import CrearTablas

class Account:
    def __init__(self):
        crearTablas = CrearTablas()
        last_id = crearTablas.get_last_id_account()  # Obtener el último ID de cuenta
        if last_id is None:
            self.id = 1  # Si no hay cuentas, establecer el ID como 1
        else:
            self.id = last_id + 1
        self.prueba = None
        self.activate = True
        self.nota = None
        self.admin=False

