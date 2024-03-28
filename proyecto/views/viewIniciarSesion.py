
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
import time 
class ViewIniciarSesion:
    textFile=ft.TextField(value="(Numero De usuario)")
    contador=ft.TextField(value="0")
    def validarUsuario(self,e):
        

        usuario=DbUsuario()
        userName=usuario.crearUsuario(self.textFile.value)
        print(userName)
        
        if userName[2][0][3] == True:
            print("es admin")
        else:
            print("no es admin")
        """page=e.control.data 
        page.clean()
        page.add(self.contador)
        for i in range(30):
            self.contador.value=str(int(self.contador.value)+1)
            time.sleep(1.2)
            page.update()"""
    
    def pestañaInicio(self,page):
        return ft.Column([
            ft.Row([ft.Text(value="Iniciar Sesion", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([self.textFile],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([ft.TextButton(text="hola ", data=page ,on_click=self.validarUsuario)],alignment=ft.MainAxisAlignment.CENTER,)        
        ])