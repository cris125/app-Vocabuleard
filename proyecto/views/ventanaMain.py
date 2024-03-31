
import flet as ft
from .viewIniciarSesion import ViewIniciarSesion
class VentanaMain:
    def iniciar(self):
        ft.app(target=self.main)

    def limpiar(self,page): 
            page.clean()
            page.add(self.interfaz(page))
            
    def pagInicio(self,e):
            page=e.control.data 
            self.limpiar(page)
            a=ViewIniciarSesion()  
            res=a.pestañaInicio(page)
            page.add(res) 

    def bienvenida(self,e):
            page=e.control.data 
            page.clean()
            page.add(self.interfaz(page))
            page.add(ft.Row([ft.Text(value="Bienvenido de vuelta", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,))

    

    def interfaz(self,page):    
            controlarInterfaz=ft.Container(ft.Row([
                ft.Container(
                        ft.OutlinedButton(text="Inicio",width=100, data=page ,on_click=self.bienvenida),
                        width=150,height=50,
                        padding=5,),
                
                ft.Container(
                        ft.OutlinedButton(text="Iniciar sesion",width=100, data=page ,on_click=self.pagInicio),
                        width=150,height=50,
                        padding=5,),
                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,),bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
            
            return controlarInterfaz 
    
    def main(self, page: ft.Page):   
        page.title = "VocaduLearn"
        page.add(self.interfaz(page))

    
         
    
    
