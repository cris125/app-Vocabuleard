from baseDeDatos.dbUsuario import DbUsuario
from views.ventanaMain import VentanaMain 
from baseDeDatos.eliminarTablas import ElimTablas
class Main:
    
    def verUsuarios(self):
        xd=DbUsuario()
        """xd.crearAdmin("1027521775")"""
        listaUsuarios=[]
        for i in xd.ver_tabla_usuario():
            infoUsuario=[]
            for x in range (len(i)):
                if x==2:
                    infoUsuario.append(xd.ver_tabla_account(i[x]))
                else:
                    infoUsuario.append(i[x])
            listaUsuarios.append(infoUsuario)    
        print(listaUsuarios)
        
"""a=Main()  
a.verUsuarios()  """
a1=  VentanaMain()
a1.iniciar()

# si el programa se descontrola
"""xd=ElimTablas()
xd.drop_table_usuario()
xd.drop_table_account()"""
