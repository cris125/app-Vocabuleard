import flet as ft
from models.Prueba import Prueba
from models.Pregunta import Pregunta
from baseDeDatos.dbPrueba import dbPrueba
import time
class ViewAgregarPrueba:
    def __init__(self,page):
        self.page=page
        self.nombrePrueba=ft.TextField(value="Nombre prueba",width=150,height=35)
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
        pregunta=ft.TextField(value="(pregunta)",height=35)
        imagen=ft.TextField(value="(imagen)",height=35)
        a=ft.TextField(value="Respuestas A",height=35)
        b= ft.TextField(value="Respuestas B",height=35)
        c=ft.TextField(value="Respuestas C",height=35)
        d=ft.TextField(value="Respuestas D",height=35)
        respuestaCorrecta=ft.TextField(value="Respuestas D",height=35)
        
        continer=ft.Container(content=ft.Column(
            [           ft.Text(value="Pregunta:",size=20),
                        pregunta,
                        ft.Text(value="imagen:"),
                        imagen,
                        ft.Text(value="Respuestas:"),
                        a, b,c,d,
                        ft.Text(value="Respuesta Correcta:"),
                        respuestaCorrecta,
                        ft.TextButton(text="Agregar Pregunta",data=(pregunta.value,[a.value,b.value,c.value,d.value],respuestaCorrecta.value,imagen.value),on_click=self.guardarPregunta)
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
        
        data=e.control.data
        newPregunta=Pregunta(data[0],data[1],data[2],data[3])
        self.newPrueba.insertarPregunta(newPregunta)
        print(data[0],data[1],data[2])
        self.preguntaView.controls.clear()
        self.preguntasGuardadas.controls.append(
            ft.Container(
                content=ft.Text(value= "pregunta "+str(len(self.preguntasGuardadas.controls)+1)+" guardada")
                ,bgcolor=ft.colors.INDIGO_100,padding=10 , border_radius=10))
        self.page.update()
   

        
        
