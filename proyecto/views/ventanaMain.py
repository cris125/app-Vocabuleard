from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
from views.viewVerUsuarios import ViewVerUsuarios
from views.viewIniciarSesion import ViewIniciarSesion
class VentanaMain:
    def __init__(self):
        ft.app(target=self.main)
    
          
    def main(self,page: ft.Page):
        def pagUsuarios(e):
            limpiar()
            a=ViewVerUsuarios()
            res=a.main()
            page.add(res)
        def pagInicio(e):
            limpiar()
            a=ViewIniciarSesion()   
            res=a.pestañaInicio(page)
            page.add(res) 

        def bienvenida(*e):
            page.clean()
            page.add(interfaz())
            page.add(ft.Row([ft.Text(value="Bienvenido de vuelta", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,))

        def limpiar(*e):
            page.clean()
            page.add(interfaz())
            
        def interfaz():    
            controlarInterfaz=ft.Container(ft.Row([
                ft.Container(
                        ft.OutlinedButton(text="Inicio",width=100,on_click=bienvenida),
                        width=150,height=50,
                        padding=5,),
                ft.Container(
                        ft.OutlinedButton(text="Ver usuarios",width=100,on_click=pagUsuarios),
                        width=150,height=50,
                        padding=5,),
                ft.Container(
                        ft.OutlinedButton(text="Iniciar sesion",width=100,on_click=pagInicio),
                        width=150,height=50,
                        padding=5,),
                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,),bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
            
            return controlarInterfaz
        
        page.title = "VocaduLearn"
        page.add(interfaz())
    
