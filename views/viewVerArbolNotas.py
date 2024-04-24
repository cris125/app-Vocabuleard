import flet as ft
from models.Arbol import Arbol
from baseDeDatos.dbUsuario import DbUsuario
import random

class ArbolNotas:

    def marizArbol(self):
        arbolBinario = Arbol()
        usuariosDb = DbUsuario()
        usuarios=usuariosDb.ver_tabla_usuario()
        
        for usuario in usuarios:
            
            
            if usuario[3] != None:
                
                arbolBinario.insertar(float(usuario[3]))

        arbol = arbolBinario.verMatriz()
        return (arbol)

    def hacerCuadros(self,texto):
        return ft.Container(content=ft.Text(value=texto,size=25,color=ft.colors.WHITE))



    def contador(self,page:ft.Page):
        column=ft.Column(alignment=ft.MainAxisAlignment.CENTER , height=page.height, width=page.width ,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        continer=ft.Container(content=column,bgcolor=ft.colors.BLUE_400)
        
        for i in self.marizArbol():
            row=ft.Row(spacing=30,
                alignment=ft.MainAxisAlignment.CENTER)
            for h in i:  
                if h=="":
                    row.controls.append(self.hacerCuadros("  "))
                row.controls.append(self.hacerCuadros(h))
                
            column.controls.append(row)
        return(continer)

