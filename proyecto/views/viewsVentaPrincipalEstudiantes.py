import flet as ft
from baseDeDatos.dbPrueba import dbPrueba
from baseDeDatos.dbUsuario import DbUsuario
import variableGlobal
import time
class VentanaPrincipalEstudiante:
    
    def intefazEstudiantes(self):
        def salir(e):
            variableGlobal.logOut()
            self.page.go("/")
           
        self.contenido=ft.Row()
        self.inter.controls.clear()
        self.inter.controls.extend([ft.Container(ft.Row([
            ft.Container(content=ft.TextButton(text="Hacer pruebas",on_click=self.verPruebas)),
            ft.Container(content=ft.TextButton(text="Ver vocabulario")),
            ft.Container(content=ft.TextButton(text="Salir",on_click=salir )),
            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
        ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15),self.contenido])
        


    def hacerPrueba(self, e ):
        self.inter.controls.clear()
        info=e.control.data
        preguntas=info[2]
        
        a=DbUsuario()
        ususario=a.getUser(variableGlobal.usuario_actual.nombre)
        for i in preguntas:
            self.pasarPreguntas(i)
        self.intefazEstudiantes() 
        print("xakskasjdjsadsa")   
        self.page.update()

    def pasarPreguntas(self, pregunta):
        
        def sigPregunta(e):
            pass
        
        def verrificarResp(e):
            hacerPregunta()
            e.control.bgcolor = "blue" if e.control.data == "true" else "red"
            e.control.update()
            self.page.update()
        def hacerPregunta():
            
            Preg=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER ,width=self.page.width)
            Preg.controls.append(ft.Text(value=pregunta["pregunta"]))
            for i in range(4):
                Preg.controls.append(ft.ElevatedButton(text=respuestas[i],data=respuestas[i],on_click=verrificarResp))
            Preg.controls.append(ft.ElevatedButton(text="siguiente pregunta",on_click=sigPregunta))
            Preg.controls.append(ft.Text(value=pregunta["respuestaCorrecta"]))
            self.page.update()
            return(Preg)
        
        self.inter.controls.clear()
        
        tiempo=ft.Text(value="0")
        temporizador=ft.Container(ft.Row([ft.Container(content=tiempo,width=150,height=50,padding=5,)],alignment=ft.MainAxisAlignment.SPACE_EVENLY,),bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
        self.inter.controls.append(temporizador)
        
        respuestas=(pregunta["respuestas"]).split(",")
        self.inter.controls.append(hacerPregunta())
        
        for i in range(10):
            time.sleep(1) 
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
        self.inter=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER ,width=self.page.width)
        self.intefazEstudiantes()
        return(self.inter)



        