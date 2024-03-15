from baseDeDatos.dbUsuario import DbUsuario
from views.ventanaVerUsuarios import VentanaVerUsuarios 
class Main:
    def verUsuarios(self):
        xd=DbUsuario()
        xd.crearUsuario("hola123")
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
xd=Main()

xd.verUsuarios()
ven=VentanaVerUsuarios()
