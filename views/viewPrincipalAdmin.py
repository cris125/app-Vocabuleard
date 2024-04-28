import flet as ft

class VentanaPrincipalAdmin:
   
        
    def salir(self,e):
        self.page.client_storage.clear()
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
            ft.Container(content=ft.TextButton(text="Ver arbol notas",on_click=lambda _: self.page.go("/pagInicioAdmin/verArbolNotas"))),
            ft.Container(content=ft.TextButton(text="Atras",on_click=self.salir))],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
        ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
        return(a)