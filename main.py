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
        
"""a=Main()
    """
def notasGeneralesEstudaintes():
    account=DbUsuario().ver_account()
    notas=[json.loads(i[1]) for i in account if i[1] != None]
    notasPro={}

    for i in notas:
        for y in i.keys():
            if y in notasPro:
                notasPro[y].extend(i[y])
            else:
                notasPro.update({y:i[y]})
    print(notasPro)
def notasPromedioPruebaSegunEstudiante(estudianteConsultado):
    usuario=DbUsuario().getUser(estudianteConsultado)
    notas=json.loads(usuario[3][0][1]) if usuario[3][0][1] != None else None 
    for i in notas.keys():
        if len(notas[i])>=2:
            notas[i]=sum(notas[i])/len(notas[i])
        else:
            notas[i]=notas[i][0]

    print(notas)

def notasDeUnaSolaPrueba():    
    usuario=DbUsuario().getUser("frank Gurrero")
    pruebaConsulta="Physics quiz"
    notas=json.loads(usuario[3][0][1]) if usuario[3][0][1] != None else None 
    for i in notas.keys():
        if i==pruebaConsulta:
            print(notas[i])



# si el programa se descontrola
"""a=ElimTablas()
a.drop_table_usuario()
a.drop_table_account()"""

