import json
import flet as ft
from baseDeDatos.dbPrueba import dbPrueba
from baseDeDatos.dbUsuario import DbUsuario
import random
import time

class VentanaPrincipalEstudiante:
    
    
    def intefazEstudiantes(self):
        def salir(e):
            self.page.client_storage.clear()
            self.page.go("/")
           
        self.contenido=ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        self.inter.controls.clear()
        self.inter.controls.extend(
            [
            ft.Container(ft.Row([
                ft.Container(content=ft.TextButton(text="Hacer pruebas",on_click=self.verPruebas)),
                ft.Container(content=ft.TextButton(text="Ver vocabulario",on_click=lambda _: self.page.go("/pagEstudioante/vocabulary"))),
                ft.Container(content=ft.TextButton(text="Ver ejercicio",on_click=lambda _: self.page.go("/pagEstudioante/ejerFrase"))),
                ft.Container(content=ft.TextButton(text="Ver progreso",on_click=lambda _: self.page.go("/pagEstudioante/Verprogreso"))),
                ft.Container(content=ft.TextButton(text="Salir",on_click=salir )),
                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)
            ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15),
            self.contenido
                ])
        
        
    def hacerPrueba(self, e ):
        self.inter.controls.clear()
        self.numPregunta=ft.Text(value="1 ",size=25)
        info=e.control.data
        preguntas=info[2]

    
        
        
        pruebas=self.ususario[2][0][1]
        
        self.calificaionPrueba=[]
        for i in preguntas:
            self.calificaionPrueba.append(self.pasarPreguntas(i))
            self.numPregunta.value=str(int(self.numPregunta.value)+1)

        if pruebas is None:
            pruebasDic={info[1]:[self.calificaionPrueba.count(True)]}
            pruebasStr=json.dumps(pruebasDic)
            self.dbUsua.actualizar_prueba(self.ususario[0],pruebasStr)
        else:
            pruebasDic=json.loads(pruebas)
            
            if info[1] in pruebasDic:
                pruebasDic[info[1]].append(self.calificaionPrueba.count(True))
            else:
                pruebasDic.update({info[1]:[self.calificaionPrueba.count(True)]})
                
            pruebasStr=json.dumps(pruebasDic)

            self.dbUsua.actualizar_prueba(self.ususario[0],pruebasStr)
            
        if self.ususario[4] != None:
            
            promedio=(float(self.ususario[4])+self.calificaionPrueba.count(True))/2
            self.dbUsua.modify_promNota(self.ususario[0],promedio)
            
        else:
            self.dbUsua.modify_promNota(self.ususario[0],self.calificaionPrueba.count(True))
            
        self.page.go("/pagEstudioante")


    def pasarPreguntas(self, pregunta):

        
        def sigPregunta(e):
            resp={"a":a,"b":b,"c":c,"d":d}
            timepoSigPerg[0]=False
            for boton in  resp.values():
                if boton.bgcolor==ft.colors.BLUE_GREY:
                    respuesta.clear()
                    respuesta.append((str(pregunta["respuestaCorrecta"]).strip() == str(boton.text).strip()))       
            self.page.update()
            
        
        def verrificarResp(e):
            sigPregun.disabled=False
            
            resp={"a":a,"b":b,"c":c,"d":d}
            boton=resp[e.control.data[1]]
            boton.bgcolor=ft.colors.BLUE_GREY
            resp.pop(e.control.data[1])
            for boton in  resp.values():
                boton.bgcolor=ft.colors.WHITE
            self.page.update()

        self.inter.controls.clear()
        timepoSigPerg=[True]
        tiempo=ft.Text(value="0",size=25)
        
        
        temporizador=ft.Container(ft.Row([
            ft.Container(content=ft.Row([
                ft.Row(
                    [ft.Text(value="Tiempo restante para pregunta:",size=25),
                    tiempo,
                    ft.Text(value="segundos de 60",size=25)]
                ),
                ft.Row(
                    [ft.Text(value=" pregunta No°",size=25),self.numPregunta]
                )
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),width=150,height=50,padding=5,)])
                                  
        ,bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
        
        self.inter.controls.append(temporizador)
        
        respuestas=(pregunta["respuestas"]).split(",")
       
        respuesta=[]
        a=ft.ElevatedButton(text=respuestas[0],data=(respuestas[0],"a"),on_click=verrificarResp)
        b=ft.ElevatedButton(text=respuestas[1],data=(respuestas[1],"b"),on_click=verrificarResp)
        c=ft.ElevatedButton(text=respuestas[2],data=(respuestas[2],"c"),on_click=verrificarResp)
        d=ft.ElevatedButton(text=respuestas[3],data=(respuestas[3],"d"),on_click=verrificarResp)
        sigPregun=ft.ElevatedButton(text="siguiente pregunta" ,on_click=sigPregunta,disabled=True)
        Preg=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER ,width=self.page.width)
        Preg.controls.append(ft.Text(value=pregunta["pregunta"]))
        Preg.controls.extend([a,b,c,d])
        Preg.controls.append(sigPregun)
        self.inter.controls.append(Preg)
        
        
        for i in range(60):
            time.sleep(1.2) 
            tiempo.value= str(int(tiempo.value)+1)
            if timepoSigPerg[0]==False:
                if len(respuesta)>0:
                    return (respuesta[0])
                else:
                    return (False)
            self.page.update()
            
        return (respuesta[0])

        

    def cuadroPrueba(self,info):
        colores=["#E05A3D","#A5E03D","#3DE093","#3DCAE0","#3D7DE0","#B43DE0","#BD8DCE","#8DCDCE","#8DCE96","#799D9E","#7C9E79"]
        content=ft.ElevatedButton(text=str(info[1])+"(hacer  prueba)", data=info ,on_click=self.hacerPrueba,bgcolor=colores[random.randrange(0,9)],color=ft.colors.WHITE)
            
        return(content)
       
    def verPruebas(self):
        a=dbPrueba()

        pruebas=a.leer_desde_base_de_datos()
        
        cuadro=ft.GridView(expand=1,
                runs_count=5,
                max_extent=250,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,)
        

        
        for prueba in pruebas:
            cuadro.controls.append(self.cuadroPrueba(prueba))
        self.contenido.controls.append(cuadro)    
        self.page.update()
        del a

    def ventanaEstudiante(self,page:ft.Page):
        self.page=page 
        self.dbUsua=DbUsuario()
        self.ususario=self.dbUsua.getUser(self.page.client_storage.get("user"))
        
        self.inter=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER )
        self.intefazEstudiantes()
        self.verPruebas()
        return(self.inter)



        