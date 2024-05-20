import flet as ft
from baseDeDatos.dbUsuario import DbUsuario
from baseDeDatos.dbPrueba import dbPrueba
import json

class MostrarProgreso:
    def venPrincipal(self,page):
        self.page=page 

        usuarioDb=DbUsuario()
        
        self.usuario=usuarioDb.getUser(page.client_storage.get("user"))

        self.contenedor=ft.Container(content=ft.Row(
            [ft.Row([ft.Container(content=self.mostrarColaTareas(),border_radius=10,border=ft.border.all(2, ft.colors.BLACK))
                ]),
            ft.Row([ft.Container(self.mostrarPilaProgreso(),border_radius=10,border=ft.border.all(2, ft.colors.BLACK)),])
                
              
             ],
            alignment=ft.MainAxisAlignment.CENTER,width=self.page.width),height=300)
        
        return(self.contenedor)
    
    def mostrarColaTareas(self):
        columna=ft.Column([],scroll=True)
        pruebasEchas=[]
        tocasLasTotales=[]
        
        if self.usuario[3][0][1] != None:
            pruebas=json.loads(self.usuario[3][0][1])
            for i in pruebas.keys():
                pruebasEchas.append(i)
         

        pruebadb=dbPrueba()
        pruebasTotales=pruebadb.leer_desde_base_de_datos()
        for i in pruebasTotales:
            tocasLasTotales.append(i[1])
        
        for i in pruebasEchas:
            tocasLasTotales.remove(i)
        
        if len(tocasLasTotales)>0: 
            for i in tocasLasTotales:
                columna.controls.append(
                    ft.Container(content=ft.Text(value="Prueba pendiente :"+str(i),size=15,color=ft.colors.BLACK)
                            ,border_radius=10,padding=5,margin=5,bgcolor="#CBDABA")
                    )
        else:
            columna.controls.append(
                        ft.Container(content=ft.Text(value="No Actividades pendientes",size=15,color=ft.colors.BLACK),
                                     border_radius=10,padding=5,margin=5,bgcolor="#A8D971"))
            
        columna.controls.insert(0,
            ft.Container(content=ft.Text(value="Pruebas Pendientes",size=25,color=ft.colors.BLUE_GREY),
                        border_radius=10,padding=5,margin=5,bgcolor="#A8D971"))
       
        return(columna)


    def mostrarPilaProgreso(self):
        columna=ft.Column(
            []
        ,scroll=True)
        if self.usuario[3][0][1] != None:
            pruebas=json.loads(self.usuario[3][0][1])
            for i in pruebas.keys():
                lista=pruebas[i]
                for x in lista:
                    columna.controls.insert(0,
                        ft.Container(content=ft.Text(value="Prueba :"+str(i)+" Nota :"+str(x),color=ft.colors.BLACK)
                            ,border_radius=10,padding=5,margin=5,bgcolor="#CBDABA")
                        
                        )
        else:
            pruebas=None
            columna.controls.append(
                        ft.Container(content=ft.Text(value="No hay Registro de actividad",size=15,color=ft.colors.BLACK)
                            ,border_radius=10,padding=5,margin=5,bgcolor="#CBDABA")
                        ) 
        columna.controls.insert(0,ft.Container(content=ft.Text(value="Pruebas Realizadas",size=25,color=ft.colors.BLUE_GREY),
                            border_radius=10,padding=5,margin=5,bgcolor="#A8D971"))    
        
        return(columna)