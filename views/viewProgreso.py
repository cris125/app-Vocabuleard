import flet as ft
from baseDeDatos.dbUsuario import DbUsuario
from baseDeDatos.dbPrueba import dbPrueba
import json
import variableGlobal
class MostrarProgreso:
    def venPrincipal(self,page):
        self.page=page 

        usuarioDb=DbUsuario()
        self.usuario=usuarioDb.getUser(variableGlobal.usuario_actual.nombre)

        self.contenedor=ft.Container(content=ft.Column([
            ft.Row([self.mostrarColaTareas(),self.mostrarPilaProgreso()]),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,scroll=True))
        return(self.contenedor)
    
    def mostrarColaTareas(self):
        columna=ft.Column(
            [ft.Container(content=ft.Text(value="Pruebas Pendientes"))]
        )
        pruebas=json.loads(self.usuario[2][0][1])
        pruebasEchas=[]
        tocasLasTotales=[]
        if pruebas is not None:
            for i in pruebas.keys():
                pruebasEchas.append(i)

        pruebadb=dbPrueba()
        pruebas=pruebadb.leer_desde_base_de_datos()
        for i in pruebas:
            tocasLasTotales.append(i[1])
        
        for i in pruebasEchas:
            tocasLasTotales.remove(i)

        for i in tocasLasTotales:
            columna.controls.append(
                ft.Container(content=ft.Text(value="Prueba pendiente :"+str(i))
                             ,border_radius=10,padding=10,margin=10,border=ft.colors.BLACK)
                )

       
        return(columna)


    def mostrarPilaProgreso(self):
        columna=ft.Column(
            [ft.Container(content=ft.Text(value="Pruebas Realizadas"))]
        )
        pruebas=json.loads(self.usuario[2][0][1])
        if pruebas is not None:
            for i in pruebas.keys():
                lista=pruebas[i]
                for x in lista:
                    columna.controls.append(
                        ft.Container(content=ft.Text(value="Prueba :"+str(i)+" Nota :"+str(x))
                                     ,border_radius=10,padding=10)
                        
                        )
                    
        
        return(columna)