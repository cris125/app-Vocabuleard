import flet as ft
from baseDeDatos.dbPrueba import dbPrueba
class VentanaPrincipalEstudiante:
    def intefazEstudiantes(self):
        self.inter=ft.Column([ft.Row([
            ft.ElevatedButton(text="Hacer pruebas"),
            ft.ElevatedButton(text="Ver vocabulario"),
        ])])
    def cuadroPrueba(self,info):
        cuadro=ft.Container(content=ft.ElevatedButton(text=info[1], data=info ), bgcolor=ft.colors.AMBER_100)
        self.inter.controls.append(cuadro)
        self.page.update()
            
    
    def ventanaEstudiante(self,page):
        self.page=page
        a=dbPrueba()
        pruebas=a.leer_desde_base_de_datos()
        
        self.intefazEstudiantes()
        for prueba in pruebas:
            self.cuadroPrueba(prueba)
        
        return(self.inter)



        