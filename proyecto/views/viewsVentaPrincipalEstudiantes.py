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
        self.calificaion=0
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
            resp={"a":a,"b":b,"c":c,"d":d}
            timepoSigPerg[0]=False
            for boton in  resp.values():
                if boton.bgcolor==ft.colors.BLUE_GREY:
                    respuesta.append((str(pregunta["respuestaCorrecta"]).strip() == str(boton.text).strip()))
                    print(respuesta)
                    print(boton)
            self.page.update()
            
        
        def verrificarResp(e):
            resp={"a":a,"b":b,"c":c,"d":d}
            boton=resp[e.control.data[1]]
            boton.bgcolor=ft.colors.BLUE_GREY
            resp.pop(e.control.data[1])
            for boton in  resp.values():
                boton.bgcolor=ft.colors.WHITE
            self.page.update()

        self.inter.controls.clear()
        timepoSigPerg=[True]
        tiempo=ft.Text(value="0")
        temporizador=ft.Container(ft.Row([ft.Container(content=tiempo,width=150,height=50,padding=5,)],alignment=ft.MainAxisAlignment.SPACE_EVENLY,),bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
        self.inter.controls.append(temporizador)
        
        respuestas=(pregunta["respuestas"]).split(",")
       
        respuesta=[]
        a=ft.ElevatedButton(text=respuestas[0],data=(respuestas[0],"a"),on_click=verrificarResp)
        b=ft.ElevatedButton(text=respuestas[1],data=(respuestas[1],"b"),on_click=verrificarResp)
        c=ft.ElevatedButton(text=respuestas[2],data=(respuestas[2],"c"),on_click=verrificarResp)
        d=ft.ElevatedButton(text=respuestas[3],data=(respuestas[3],"d"),on_click=verrificarResp)

        Preg=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER ,width=self.page.width)
        Preg.controls.append(ft.Text(value=pregunta["pregunta"]))
        Preg.controls.extend([a,b,c,d])
        Preg.controls.append(ft.ElevatedButton(text="siguiente pregunta" ,on_click=sigPregunta))
        Preg.controls.append(ft.Text(value=pregunta["respuestaCorrecta"]))
        self.inter.controls.append(Preg)
        
        
        for i in range(10):
            time.sleep(1) 
            tiempo.value= str(int(tiempo.value)+1)
            if timepoSigPerg[0]==False:
                return 
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



        