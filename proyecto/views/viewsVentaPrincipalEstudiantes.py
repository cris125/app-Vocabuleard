import flet as ft
from baseDeDatos.dbPrueba import dbPrueba
import time
class VentanaPrincipalEstudiante:
    
    def intefazEstudiantes(self):
        self.contenido=ft.Row()
        self.inter=ft.Column([ft.Container(ft.Row([
            ft.Container(content=ft.TextButton(text="Hacer pruebas",on_click=self.verPruebas)),
            ft.Container(content=ft.TextButton(text="Ver vocabulario")),
            ft.Container(content=ft.TextButton(text="Salir",on_click=lambda _: self.page.go("/"))),
            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
        ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15), self.contenido],width=self.page.width)


    def hacerPrueba(self, e ):
        self.inter.controls.clear()
        info=e.control.data
        preguntas=info[2]
        for i in preguntas:
            self.pasarPreguntas(i)
        self.intefazEstudiantes()    
        self.page.update()

    def pasarPreguntas(self, pregunta):
        self.inter.controls.clear()
        tiempo=ft.Text(value="1")
        temporizador=ft.Container(ft.Row([
            ft.Container(content=tiempo,width=150,height=50,
                        padding=5,)
            
            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,),bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)



        self.inter.controls.clear()
        self.inter.controls.append(
            temporizador
        )
        self.inter.controls.append(
            ft.Row([
                ft.Text(value=pregunta["pregunta"]),
                ft.Text(value=pregunta["pregunta"])
            ]))
        for i in range(10):
            time.sleep(1.5) 
            tiempo.value= str(int(tiempo.value)+1) 
            self.page.update()
        

    def cuadroPrueba(self,info):
        cuadro=ft.Container(content=ft.ElevatedButton(text=str(info[1])+"(hacer  prueba)", data=info ,on_click=self.hacerPrueba), bgcolor=ft.colors.AMBER_100)
        self.contenido.controls.append(cuadro)
        
            
    def verPruebas(self,e):
        a=dbPrueba()
        pruebas=a.leer_desde_base_de_datos()
        for prueba in pruebas:
            self.cuadroPrueba(prueba)
        self.page.update()

    def ventanaEstudiante(self,page:ft.Page):
        self.page=page 
        self.intefazEstudiantes()
        return(self.inter)



        