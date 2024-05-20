
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
import asyncio

class ViewIniciarSesion:
    textFileUserName=ft.TextField(label="(Nomrbre de usuario)")
    textFilePassword=ft.TextField(label="Contraseña",password=True, can_reveal_password=True)
    contenido=ft.Row(alignment=ft.MainAxisAlignment.CENTER)

    def validarUsuario(self,e):
        e.control.disabled=True
        self.page.update()
        asyncio.run(self.validarUsuarioAsuncrona())
        
    async def getDbUsuario(self):
        usuario=DbUsuario()
        usuarioExist=usuario.verificar_usuario(self.textFileUserName.value)
        """userName=usuario.crearUsuario(self.textFileUserName.value,self.textFilePassword)"""

        await asyncio.sleep(1)
        self.contenido.controls.clear()
        if usuarioExist:
            userName=usuario.getUser(self.textFileUserName.value)
            print(userName)
            if userName[2][0][3] == True:
                self.page.client_storage.set("user", self.textFileUserName.value)
                self.page.client_storage.set("is_admin", True)
                
                print("es admin")
                self.page.go("/pagInicioAdmin/contrasena")
            else:
                self.page.client_storage.set("user", self.textFileUserName.value)
                self.page.client_storage.set("is_admin", False)
                

                self.page.go("/pagEstudioante")
                print("no es admin")
        else:
            print("usuario no existe")
        
    async def mensajeCargar(self):
        self.contenido.controls.append(
            ft.Text(value="Cargando...",size=25)
        )
        self.page.update()

    async def validarUsuarioAsuncrona(self):
        tareas=[]
        tareas.append(asyncio.create_task(self.mensajeCargar()))
        tareas.append(asyncio.create_task(self.getDbUsuario()))
        await asyncio.gather(*tareas)

        
        
    
    def pestañaInicio(self,page):
        self.page=page
        return ft.Column([
            ft.Row([ft.Text(value="Iniciar Sesion", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([self.textFileUserName],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([self.textFilePassword],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([ft.TextButton(text="ingresar",on_click=self.validarUsuario)] ,alignment=ft.MainAxisAlignment.CENTER,  )        
            ,self.contenido
        ])