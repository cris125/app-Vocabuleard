
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
import variableGlobal

class ViewIniciarSesion:
    textFile=ft.TextField(value="(Numero De usuario)")
    contador=ft.TextField(value="0")

    def validarUsuario(self,e):
    
        usuario=DbUsuario()
        userName=usuario.crearUsuario(self.textFile.value)
        print(userName)
        if userName[2][0][3] == True:
            variableGlobal.establecer_usuario_actual(self.textFile.value, admin=True)
            print("es admin")
            self.page.go("/pagInicioAdmin")
        else:
            variableGlobal.establecer_usuario_actual(self.textFile.value, admin=False)
            self.page.go("/pagEstudioante")
            print("no es admin")
        
    
    def pestañaInicio(self,page):
        self.page=page
        return ft.Column([
            ft.Row([ft.Text(value="Iniciar Sesion", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([self.textFile],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([ft.TextButton(text="ingresar",on_click=self.validarUsuario)] ,alignment=ft.MainAxisAlignment.CENTER,  )        
        ])