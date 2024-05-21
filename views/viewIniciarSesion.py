
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
import time
import hashlib

class ViewIniciarSesion:
    textFileUserName=ft.TextField(label="(Nombre de usuario)")
    textFilePassword=ft.TextField(label="Contraseña",password=True, can_reveal_password=True)
    contenido=ft.Row(alignment=ft.MainAxisAlignment.CENTER)

    def validarUsuario(self,e):
        """self.page.update()"""
        self.getDbUsuario()
        """if res==1:"""
            
        
    def getDbUsuario(self):
        usuario=DbUsuario()
        usuarioExist=usuario.verificar_usuario(self.textFileUserName.value) 
        
        """userName=usuario.crearUsuario(self.textFileUserName.value,self.textFilePassword)"""

        self.contenido.controls.clear()
        
        if usuarioExist:
            userName=usuario.getUser(self.textFileUserName.value) 
            contasenaCorrecta=self.hacerContrasena(self.textFilePassword.value) == userName[2]

            if contasenaCorrecta:
                if userName[3][0][3] == True:
                    self.page.client_storage.set("user", self.textFileUserName.value)
                    self.page.client_storage.set("is_admin", True)
                    
                    self.page.go("/pagInicioAdmin")
                    print("es admin")
                else:
                    self.page.client_storage.set("user", self.textFileUserName.value)
                    self.page.client_storage.set("is_admin", False)

                    self.page.go("/pagEstudioante")
                    print("no es admin")
            else:
                self.mensajeContraInco()
                print("contraseña incorrecta")
                return(1)
        else:
            self.mensajeContraInco()
            print("Este usuario no existe")
            return(1)
        
    def mensajeContraInco(self):
        self.contenido.controls.append(
            ft.Text(value="Contraseña o Usuario Incorrecto",size=15,color=ft.colors.RED_500)
        )
        self.page.update()
        time.sleep(2)
        self.contenido.controls.pop(-1)
        self.page.update()

    def hacerContrasena(self,contrasena:str):
        m = hashlib.sha256()
        m.update(contrasena.encode())
        return m.hexdigest()    
        
    
    def pestañaInicio(self,page):
        self.page=page
        return ft.Column([
            ft.Row([ft.Text(value="Iniciar Sesion", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([self.textFileUserName],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([self.textFilePassword],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([ft.TextButton(text="ingresar",on_click=self.validarUsuario)] ,alignment=ft.MainAxisAlignment.CENTER,  )        
            ,self.contenido
        ])