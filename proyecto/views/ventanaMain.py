from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
from views.viewVerUsuarios import ViewVerUsuarios

class VentanaMain:
    def __init__(self):
        ft.app(target=self.main)
    
          
    def main(self,page: ft.Page):
        def pagUsuarios(e):
            limpiar()
            a=ViewVerUsuarios()
            res=a.main()
            page.add(res)
            
        def limpiar(*e):
            page.clean()
            page.add(interfaz())
            
        def interfaz():    
            controlarInterfaz=ft.Container(ft.Row([
                ft.Container(
                        ft.OutlinedButton(text="Inicio",width=100,on_click=limpiar),
                        width=150,height=50,
                        padding=5,),
                ft.Container(
                        ft.OutlinedButton(text="Ver usuarios",width=100,on_click=pagUsuarios),
                        width=150,height=50,
                        padding=5,),
                ft.Container(
                        ft.OutlinedButton(text="Iniciar secion",width=100),
                        width=150,height=50,
                        padding=5,),
                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,),bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
            
            return controlarInterfaz
        
        page.title = "VocaduLearn"
        page.add(interfaz())
    
