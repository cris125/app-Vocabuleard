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
    

"""notas=[json.loads(i[1]) for i in account if i[1] != None]
notasPro=[]
for i in notas:
    for h in i.values():
        notasPro.extend(h)
"""
# si el programa se descontrola
"""a=ElimTablas()
a.drop_table_usuario()
a.drop_table_account()"""

