import flet as ft
from .viewVerUsuarios import ViewVerUsuarios
import variableGlobal
class VentanaPrincipalAdmin:
    def pagUsuarios(self):
            a=ViewVerUsuarios()
            res=a.main()
            return(res)
        
    def salir(self,e):
        variableGlobal.logOut()
        self.page.go("/")
              
    def ventanaAdmin(self,page):
        self.page=page
        self.verUsuarios=[]
        
          

        a=ft.Container(ft.Row([
            ft.Container(content=ft.TextButton(text="Ver Usuarios",on_click=lambda _: self.page.go("/pagInicioAdmin/verUsuarios"))),
            ft.Container(content=ft.TextButton(text="Agregar Administrador",on_click=lambda _: self.page.go("/pagInicioAdmin/agregarAdmin"))),
            ft.Container(content=ft.TextButton(text="Agregar Prueba",on_click=lambda _: self.page.go("/pagInicioAdmin/agregarPrueba"))),
            ft.Container(content=ft.TextButton(text="Eliminar Usuarios",on_click=lambda _: self.page.go("/pagInicioAdmin/eliminarUsuario"))),
            ft.Container(content=ft.TextButton(text="Ver pruebas",on_click=lambda _: self.page.go("/pagInicioAdmin/verPruebas"))),
            
            ft.Container(content=ft.TextButton(text="Atras",on_click=self.salir))],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
        ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
        return(a)