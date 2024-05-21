from baseDeDatos.dbUsuario import DbUsuario
from views.ventanaMain import VentanaMain 
from baseDeDatos.eliminarTablas import ElimTablas
import json
class Main:
    def __init__(self) -> None:
        e=DbUsuario()
        e.crearAdmin("admin1","admin")
        a1=  VentanaMain()
        a1.iniciar()
a=Main()

"""print(notasGeneralesEstudaintes()[1])"""
"""notasGeneralesEstudaintes()"""
"""notasPromedioPruebaSegunEstudiante("daniel hidalgo")"""
"""notasDeUnaSolaPrueba()"""
# si el programa se descontrola
"""a=ElimTablas()
a.drop_table_usuario()
a.drop_table_account()"""

