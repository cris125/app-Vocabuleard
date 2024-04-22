from baseDeDatos import dbPrueba
import flet as ft
import time
class EliminarPrueba():
    def eliminarPrueba(self,e):
        a=dbPrueba()
        prueba=a.verificar_prueba(self.usuarioElim.value)
        if prueba is not None:
            a.eliminar_prueba(self.usuarioElim.value)
            self.vetana.controls.clear()
            self.vetana.controls.append(ft.Text(value="La prueba fue eliminado correctamente",size=35))
            self.page.update()
            time.sleep(2)
            self.page.go("/pagInicioAdmin")
        else:
            self.vetana.controls.clear()
            self.vetana.controls.append(ft.Text(value="El prueba no existe",size=35))
            self.page.update()
            time.sleep(2)
            self.page.go("/pagInicioAdmin")
                 
            

        
    def ventanaEliminarPrueba(self,page):
        self.page=page
        self.usuarioElim=ft.TextField("(Id prueba)")
        self.vetana=ft.Column([ft.Text(value="Ingrese el id que quiere eliminar"),
                          self.usuarioElim
                          ,ft.ElevatedButton(text="eliminar prueba",on_click=self.eliminarPrueba)]
                         ,scroll=True, alignment=ft.alignment.center)
        return(self.vetana)