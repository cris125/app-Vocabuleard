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

        self.pilaProgreso=self.mostrarPilaProgreso()
        self.contenedor=ft.Container(ft.Column([
            ft.Row(self.pilaProgreso),
            ft.Row()
        ]))
    
    def mostrarColaTareas(self):
        pruebas=json.loads(self.usuario[2][0][1])
        pruebasEchas=[]
        tocasLasTotales=[]
        if pruebas is not None:
            for i in pruebas.keys():
                pruebasEchas.append(i)
                
        else:
            pruebadb=dbPrueba
            pruebas=pruebadb.leer_desde_base_de_datos()

        return(ft.Text("xd"))


    def mostrarPilaProgreso(self):
        
        pruebas=json.loads(self.usuario[2][0][1])
        if pruebas is not None:
            for i in pruebas.keys():
                lista=pruebas[i]
                for x in lista:
                    print(i,x)
        
        return(ft.Text("xd"))