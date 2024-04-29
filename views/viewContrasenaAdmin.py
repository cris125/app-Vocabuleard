import flet as ft 
import time
class ContrasenaAdmin:
    def pedirContraseña(self,page:ft.Page):
        self.row=ft.Row(alignment=ft.MainAxisAlignment.CENTER)

        def resetearError(e):
            self.row.controls.clear()
            self.row.controls.extend([self.contraseña,sumit])
            page.update()
        
        def validarContraseña(e):
            if self.contraseña.value != "admin":
                self.row.controls.append(self.textError)
                page.update()
                time.sleep(2)
                self.row.controls.clear()
                self.row.controls.extend([self.contraseña,sumit])
                page.update()

            else:
                page.go("/pagInicioAdmin")


        self.contraseña=ft.TextField(
            label="pasword", password=True, can_reveal_password=True
        )
        sumit=ft.ElevatedButton(text="ingresar",data=self.contraseña,on_click=validarContraseña)
        self.textError=ft.Text(value="Contraseña Incorrecta",color=ft.colors.RED_300)
        
        self.row.controls.clear()
        self.row.controls.extend([self.contraseña,sumit])

        return(self.row)