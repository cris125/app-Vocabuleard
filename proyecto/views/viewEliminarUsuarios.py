import flet as ft 
from baseDeDatos.dbUsuario import DbUsuario
class EliminarUsuarios:
    
    def eliminarUsuario(self,e):
        a=DbUsuario()
        usuario=a.getUser(self.usuarioElim.value)
        print(usuario)
        """a.eliminar_usuario(usuario[0],usuario[2][0])"""
        self.vetana.controls.clear()
        self.vetana.controls.append(ft.Text(value="El Usuario fue eliminado Correctamente",size=35))
        self.page.update()
    def ventanaEliminarUsuario(self,page):
        self.page=page
        self.usuarioElim=ft.TextField("(codigo del usuario)")
        self.vetana=ft.Column([ft.Text(value="Ingrese el usuario que quiere eliminar"),
                          self.usuarioElim
                          ,ft.ElevatedButton(text="eliminar Usuario",on_click=self.eliminarUsuario)]
                         ,scroll=True, alignment=ft.alignment.center)
        return(self.vetana)