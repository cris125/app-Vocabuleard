import flet as ft 
from baseDeDatos.dbUsuario import DbUsuario
class AgregarAdministradores:
    
    def agregarAdmin(self,e):
        a=DbUsuario()
        a.crearAdmin(self.newAdmin.value)
        self.vetana.controls.clear()
        self.vetana.controls.append(ft.Text(value="El administador fue agregado Correctamente",size=35))
        self.page.update()
    def ventanaAgreAdmin(self,page):
        self.page=page
        self.newAdmin=ft.TextField("(codigo del usuario)")
        self.vetana=ft.Column([ft.Text(value="Ingrese el usuario que quiere crear"),
                          self.newAdmin
                          ,ft.ElevatedButton(text="Agregar Admin",on_click=self.agregarAdmin)]
                         ,scroll=True, alignment=ft.alignment.center)
        return(self.vetana)