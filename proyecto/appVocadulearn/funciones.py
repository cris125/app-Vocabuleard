from baseDeDatos.dbUsuario import DbUsuario
from models.usuario import Usuario

class Main:
    def vertabla(self):
        xd=DbUsuario()
        xd.crearUsuario("diego1")
        for i in xd.ver_tabla_usuario():
            txt=[]
            for x in range (len(i)):
                if x==2:
                    txt.append(xd.ver_tabla_account(i[x]))
                else:

                    txt.append(i[x])
            print(txt)
xd=Main()
xd.vertabla()