
import flet as ft

class InterfazUsuario:
    def hacerintefazEstudiantes(self,page:ft.Page):
        def salir(e):
            page.client_storage.clear()
            page.go("/")
        
        interfaz=ft.Container(ft.Row([
                ft.Container(content=ft.TextButton(text="Hacer pruebas",on_click=lambda _: page.go("/pagEstudioante/hacerPrueba"))),
                ft.Container(content=ft.TextButton(text="Ver vocabulario",on_click=lambda _: page.go("/pagEstudioante/vocabulary"))),
                ft.Container(content=ft.TextButton(text="Ver ejercicio",on_click=lambda _: page.go("/pagEstudioante/ejerFrase"))),
                ft.Container(content=ft.TextButton(text="Ver progreso",on_click=lambda _: page.go("/pagEstudioante/Verprogreso"))),
                ft.Container(content=ft.TextButton(text="Salir",on_click=salir )),
                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
            ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
                
        return(interfaz)