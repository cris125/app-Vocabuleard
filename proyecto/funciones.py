from baseDeDatos.dbUsuario import DbUsuario
from views.ventanaMain import VentanaMain 
from baseDeDatos.eliminarTablas import ElimTablas
class Main:
    def __init__(self) -> None:
        a1=  VentanaMain()
        a1.iniciar()
        
a=Main()  


# si el programa se descontrola
"""xd=ElimTablas()
xd.drop_table_usuario()
xd.drop_table_account()"""
