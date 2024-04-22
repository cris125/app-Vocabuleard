from baseDeDatos.dbPrueba import dbPrueba
import flet as ft
class VerPruebas:
    def cuadroPrincipal(self):
        self.cuadroPruebas=ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=120,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,)
    # cuadro con container que tencagn cada prueba
    def cuadroPrueba(self,info):
        cuadro=ft.Container(content=ft.ElevatedButton(text=info[1], data=info ,on_click=self.abrirPrueba ), bgcolor=ft.colors.AMBER_100)
        self.cuadroPruebas.controls.append(cuadro)
        self.page.update()
        
        
    def abrirPrueba(self,e):
        
        infoPrueba=e.control.data
        self.cuadroPruebas.controls.clear()
        self.cuadroPruebas.controls.append(
            ft.Row([ft.Text(value=str(infoPrueba))])
            )
        self.page.update()
        
    def pruebas(self,page:ft.Page):
        self.page=page
        a=dbPrueba()
        pruebas=a.leer_desde_base_de_datos()
        
        self.cuadroPrincipal()
        for prueba in pruebas:
            self.cuadroPrueba(prueba)
            
        return(self.cuadroPruebas)
        
        
   