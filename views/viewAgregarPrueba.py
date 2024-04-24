import flet as ft
from models.Prueba import Prueba
from models.Pregunta import Pregunta
from baseDeDatos.dbPrueba import dbPrueba
import time
class ViewAgregarPrueba:
    def __init__(self,page):
        self.page=page
        self.nombrePrueba=ft.TextField(value="Nombre prueba",width=300,height=60)
        self.newPrueba=Prueba()
        self.preguntaView=ft.Row(alignment=ft.MainAxisAlignment.CENTER,width= self.page.width)
        self.preguntasGuardadas = ft.Row(scroll=True)
        self.preguntasGuardadasArray=[]
        
    def guardarPrueba(self,e):
        self.preguntaView.controls.clear()
        self.preguntasGuardadas.controls.clear()
        
        self.newPrueba.setNombre(self.nombrePrueba.value)

        a=dbPrueba()
        a.guardar_en_base_de_datos(self.newPrueba)
        self.preguntasGuardadas.controls.append(ft.Text(value="La pregunta se guardo",size=20))
        time.sleep(2)
        self.page.go("/pagInicioAdmin")
        
    def AgregarOtraPregunta(self,e):
        self.pregunta=ft.TextField(value="(pregunta)")
        self.imagen=ft.TextField(value="(imagen)")
        self.a=ft.TextField(value="Respuestas A")
        self.b= ft.TextField(value="Respuestas B")
        self.c=ft.TextField(value="Respuestas C")
        self.d=ft.TextField(value="Respuestas D")
        self.respuestaCorrecta=ft.TextField(value="Respuestas D")
        
        continer=ft.Container(content=ft.Column(
            [           ft.Text(value="Pregunta:",size=20),
                        self.pregunta,
                        ft.Text(value="imagen:"),
                        self.imagen,
                        ft.Text(value="Respuestas:"),
                        self.a, self.b,self.c,self.d,
                        ft.Text(value="Respuesta Correcta:"),
                        self.respuestaCorrecta,
                        ft.TextButton(text="Guardar Pregunta",on_click=self.guardarPregunta)
             ],scroll=True,width= self.page.width,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ,border=ft.border.all(2, ft.colors.BLACK), border_radius=5,padding=5,width=500,height=450)
        self.preguntaView.controls.append(continer)
        self.page.update()
        
    def prueba(self):
        self.preguntaView.controls.clear()
        
        intefaz=ft.Row([ft.Column([
            ft.Row([
                ft.TextButton(text="Agregar Otra pregunta", on_click=self.AgregarOtraPregunta),
                ft.TextButton(text="Guardar Prueba",on_click=self.guardarPrueba),
                ft.TextButton(text="Eliminar Pruebas (Segun id)",on_click=lambda _: self.page.go("/pagInicioAdmin/eliminarPrueba")),
                ft.Text(value="Nombre de purba: ",size=15),
                self.nombrePrueba
                ]),
                ft.Row([self.preguntasGuardadas],alignment=ft.MainAxisAlignment.CENTER,),
                ft.Row([self.preguntaView],alignment=ft.MainAxisAlignment.CENTER,)
                
            ],alignment=ft.alignment.center,
            ),],alignment=ft.MainAxisAlignment.CENTER,scroll=True)
        
        return(intefaz)
    
    def guardarPregunta(self,e):
        print((self.pregunta.value,
                             [self.a.value , self.b.value , self.c.value , self.d.value],
                             self.respuestaCorrecta.value,
                             self.imagen.value))
        
        newPregunta=Pregunta(self.pregunta.value,
                             [self.a.value , self.b.value , self.c.value , self.d.value],
                             self.respuestaCorrecta.value,
                             self.imagen.value)
        self.newPrueba.insertarPregunta(newPregunta)
        self.preguntaView.controls.clear()
        self.preguntasGuardadas.controls.append(
            ft.Container(
                content=ft.Text(value= "pregunta "+str(len(self.preguntasGuardadas.controls)+1)+" guardada")
                ,bgcolor=ft.colors.INDIGO_100,padding=10 , border_radius=10))
        self.page.update()
   

        
        
