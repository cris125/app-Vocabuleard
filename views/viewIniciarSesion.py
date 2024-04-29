
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
import asyncio

class ViewIniciarSesion:
    textFile=ft.TextField(label="(Numero De usuario)")
    contenido=ft.Row(alignment=ft.MainAxisAlignment.CENTER)

    def validarUsuario(self,e):
        e.control.disabled=True
        self.page.update()
        asyncio.run(self.validarUsuarioAsuncrona())
        
    async def getDbUsuario(self):
        usuario=DbUsuario()
        userName=usuario.crearUsuario(self.textFile.value)

        await asyncio.sleep(3)
        self.contenido.controls.clear()
        
        print(userName)
        if userName[2][0][3] == True:
            self.page.client_storage.set("user", self.textFile.value)
            self.page.client_storage.set("is_admin", True)
            
            print("es admin")
            self.page.go("/pagInicioAdmin/contrasena")
        else:
            self.page.client_storage.set("user", self.textFile.value)
            self.page.client_storage.set("is_admin", False)
            

            self.page.go("/pagEstudioante")
            print("no es admin")
        
        
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
            ft.Row([self.textFile],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([ft.TextButton(text="ingresar",on_click=self.validarUsuario)] ,alignment=ft.MainAxisAlignment.CENTER,  )        
            ,self.contenido
        ])