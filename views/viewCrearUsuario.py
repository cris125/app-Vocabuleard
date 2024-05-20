import flet as ft 
import time

from baseDeDatos.dbUsuario import DbUsuario
class CrearUsuario:
    def crearUser(self,page:ft.Page):

        def menajeError(mensaje:str):
            mesajeError=ft.Row([ft.Text(value=mensaje,color=ft.colors.RED_400, size=18)],alignment=ft.MainAxisAlignment.CENTER,)
            self.colum.controls.append(mesajeError)
            page.update()
            time.sleep(2)
            self.colum.controls.pop(-1)
            page.update()     

        def mensajeCarga():
            mesajeError=ft.Row([ft.Text(value="Cargando ...", size=18)],alignment=ft.MainAxisAlignment.CENTER,)
            self.colum.controls.append(mesajeError)
            page.update()
            
        
        def validarContraseña(e):
            
            if self.usuarioDb.verificar_usuario(self.username.value):
                menajeError("Este usuario ya existe")
            else:
                if self.contraseña.value == self.contraseñaConfirm.value and self.contraseña.value!="":
                    mensajeCarga()
                    self.usuarioDb.crearUsuario(self.username.value,self.contraseña.value)
                    page.client_storage.set("user", self.username.value)
                    page.client_storage.set("is_admin", False)
                    
                    page.go("/pagEstudioante")

                else:
                    menajeError("Las contraseñas no coinciden")
                    
        self.usuarioDb=DbUsuario()

        self.username=ft.TextField(label="Nombre Usuario")
        self.contraseña=ft.TextField(
            label="Contraseña", password=True, can_reveal_password=True
        )
        self.contraseñaConfirm=ft.TextField(
            label="Confirmar Contraseña", password=True, can_reveal_password=True
        )

        
        
        sumit=ft.ElevatedButton(text="Crear Usuario",on_click=validarContraseña)

        self.colum=ft.Column(
            [ 
            ft.Row([self.username],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.contraseña],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.contraseñaConfirm],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([sumit],alignment=ft.MainAxisAlignment.CENTER)
            ],alignment=ft.MainAxisAlignment.CENTER)

        


        return(self.colum)