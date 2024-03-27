
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft

class ViewIniciarSesion:
    textFile=ft.TextField(value="1235")
    def validarUsuario(self,e):
        print(self.textFile.value)   
        
    def pestañaInicio(self):
        return ft.Column([
            ft.Row([ft.Text(value="Iniciar Secion", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([self.textFile],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([ft.TextButton(text="hola ", data=self.textFile.value,on_click=self.validarUsuario)],alignment=ft.MainAxisAlignment.CENTER,)
               
            
        ])