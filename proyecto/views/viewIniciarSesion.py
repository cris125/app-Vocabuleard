
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
import variableGlobal
import asyncio
class ViewIniciarSesion:
    textFile=ft.TextField(value="(Numero De usuario)")
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

        if userName[2][0][3] == True:
            variableGlobal.establecer_usuario_actual(self.textFile.value, admin=True)
            print("es admin")
            self.page.go("/pagInicioAdmin")
        else:
            variableGlobal.establecer_usuario_actual(self.textFile.value, admin=False)
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