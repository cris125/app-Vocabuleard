from baseDeDatos.dbUsuario import DbUsuario
import flet as ft

class VentanaVerUsuarios:
    def consultarUsuarios(self):
        db=DbUsuario()
        listaUsuarios=[]
        for i in db.ver_tabla_usuario():
            infoUsuario=[]
            for x in range (len(i)):
                if x==2:
                    infoUsuario.append(db.ver_tabla_account(i[x]))
                else:
                    infoUsuario.append(i[x])
            listaUsuarios.append(infoUsuario)  
        return(listaUsuarios)
    
    def __init__(self):
        ft.app(target=self.main)
        
    def main(self,page: ft.Page):
        page.title = "ver Usuarios"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        txt_number = ft.TextField(value=str(self.consultarUsuarios()), text_align=ft.TextAlign.RIGHT, width=100)
        
        def verUsuarios(e):
            
            page.clean()
            
            h=[txt_number,]
            xd=ft.Column(h)
            page.add(xd)
            
            page.update()
            
        h=[
        txt_number,
        ft.IconButton(ft.icons.ADD, on_click=verUsuarios),]
         
        xd=ft.Row(h)
        
        page.add(
           txt_number
        )

xd=VentanaVerUsuarios()