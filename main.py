from baseDeDatos.dbUsuario import DbUsuario
from views.ventanaMain import VentanaMain 
from baseDeDatos.eliminarTablas import ElimTablas
class Main:
    def __init__(self) -> None:
        e=DbUsuario()
        e.crearAdmin("admin1")
        a1=  VentanaMain()
        a1.iniciar()
        
a=Main()


# si el programa se descontrola
"""a=ElimTablas()
a.drop_table_usuario()
a.drop_table_account()
a.drop_table_pruebas()"""
