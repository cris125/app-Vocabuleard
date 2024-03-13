from views.viwUsuario import ViwUsuario
from models.usuario import Usuario
xd=ViwUsuario()
pepe=Usuario("pe1")

xd.crearUsuario("pepe")
for i in xd.ver_tabla_usuario():
    txt=[]
    for x in range (len(i)):
        if x==2:
            txt.append(xd.ver_tabla_account(i[x]))
        else:

            txt.append(i[x])
    print(txt)