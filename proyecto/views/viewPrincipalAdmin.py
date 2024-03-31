import flet as ft
from .viewVerUsuarios import ViewVerUsuarios

class VentanaPrincipalAdmin:
    def ventanaAdmin(self,page):
        def pagUsuarios(e):
            limpiar()
            a=ViewVerUsuarios()
            res=a.main()
            page.add(res)
        def limpiar():
            page.clean()
            page.add(a)
        
        def salir(e):
            pass

            
        a=ft.Container(ft.Row([
            ft.Container(content=ft.TextButton(text="Ver Usuarios",on_click=pagUsuarios)),
            ft.Container(content=ft.TextButton(text="Eliminar Usuarios")),
            ft.Container(content=ft.TextButton(text="Atras",on_click=salir))],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
        ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
        page.clean()
        page.add(a)