import flet as ft 
from baseDeDatos.dbUsuario import DbUsuario
import time
class EliminarUsuarios:
    
    def eliminarUsuario(self,e):
        a=DbUsuario()
        usuario=a.getUser(self.usuarioElim.value)
        if usuario is not None:
            a.eliminar_usuario(int(usuario[0]),int(usuario[2][0][0]))
            self.vetana.controls.clear()
            self.vetana.controls.append(ft.Text(value="El usuario fue eliminado correctamente",size=35))
            self.page.update()
            time.sleep(2)
            self.page.go("/pagInicioAdmin")
        else:
            self.vetana.controls.clear()
            self.vetana.controls.append(ft.Text(value="El usuario no existe",size=35))
            self.page.update()
            time.sleep(2)
            self.page.go("/pagInicioAdmin")
                 
            

        
    def ventanaEliminarUsuario(self,page):
        self.page=page
        self.usuarioElim=ft.TextField("(codigo del usuario)")
        self.vetana=ft.Column([ft.Text(value="Ingrese el usuario que quiere eliminar"),
                          self.usuarioElim
                          ,ft.ElevatedButton(text="eliminar Usuario",on_click=self.eliminarUsuario)]
                         ,scroll=True, alignment=ft.alignment.center)
        return(self.vetana)