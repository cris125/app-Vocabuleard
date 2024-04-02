import flet as ft 
from baseDeDatos.dbUsuario import DbUsuario
class AgregarAdministradores:
    
    def agregarAdmin(self,e):
        a=DbUsuario()
        a.crearAdmin(self.newAdmin.value)
        print(self.newAdmin.value )

    def ventanaAgreAdmin(self):
        self.newAdmin=ft.TextField("(codigo del usuario)")
        vetana=ft.Column([ft.Text(value="Ingrese el usuario que quiere crear"),
                          self.newAdmin
                          ,ft.ElevatedButton(text="Agregar Admin",on_click=self.agregarAdmin)]
                         ,scroll=True, alignment=ft.alignment.center)
        return(vetana)