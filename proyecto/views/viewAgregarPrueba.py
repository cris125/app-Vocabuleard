import flet as ft
from models.Prueba import Prueba
class ViewAgregarPrueba:
    def __init__(self,page):
        self.page=page
        self.preguntaView=ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        self.preguntasGuardadas = ft.Column()
        self.preguntasGuardadasArray=[]
        
    def AgregarOtraPregunta(self,e):
        pregunta=ft.TextField(value="(pregunta)",height=35)
        a=ft.TextField(value="Respuestas A",height=35)
        b= ft.TextField(value="Respuestas B",height=35)
        c=ft.TextField(value="Respuestas C",height=35)
        d=ft.TextField(value="Respuestas D",height=35)
        respuestaCorrecta=ft.TextField(value="Respuestas D",height=35)
        
        continer=ft.Container(content=ft.Column(
            [           ft.Text(value="Pregunta:",size=20),
                        pregunta,
                        ft.Text(value="Respuestas:"),
                        a, b,c,d,
                        ft.Text(value="Respuesta Correcta:"),
                        respuestaCorrecta,
                        ft.TextButton(text="Agregar Pregunta",data=(a,b,c,d,respuestaCorrecta),on_click=self.guardarPregunta)
             ],scroll=ft.ScrollMode.ALWAYS)
                ,border=ft.border.all(2, ft.colors.BLACK), border_radius=5,padding=5,width=500)
        self.preguntaView.controls.append(continer)
        self.page.update()
        
    def prueba(self):
        nombrePrueba=ft.TextField(value="Nombre prueba",width=150,height=35)
        intefaz=ft.Row([ft.Column([
            ft.Row([
                ft.TextButton(text="Agregar Otra pregunta", on_click=self.AgregarOtraPregunta),
                ft.TextButton(text="Guardar Prueba"),
                ft.Column([ft.Text(value="Nombre de purba: ",size=15),nombrePrueba]), 
                ]),
                ft.Row([self.preguntasGuardadas],alignment=ft.MainAxisAlignment.CENTER,),
                ft.Row([self.preguntaView],alignment=ft.MainAxisAlignment.CENTER,)
            ]),
            ],alignment=ft.MainAxisAlignment.CENTER,)
        return(intefaz)
    
    def guardarPregunta(self,e):
        self.preguntaView.controls.clear()
        self.preguntasGuardadas.controls.append(ft.Text(value=str(e.control.data)))
        self.page.update()
   

        
        
