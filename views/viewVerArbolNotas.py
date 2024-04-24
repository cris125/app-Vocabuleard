import flet as ft
from models.Arbol import Arbol

import random

class ArbolNotas:

    def marizArbol(self):
        arbolBinario = Arbol()
        for i in range(20):
            
            arbolBinario.insertar(random.randint(0,10))
    
        usuario = arbolBinario.verMatriz()
        return (usuario)

    def hacerCuadros(self,texto):
        return ft.Container(content=ft.Text(value=texto,size=25,color=ft.colors.WHITE))



    def contador(self,page:ft.Page):
        column=ft.Column(alignment=ft.MainAxisAlignment.CENTER,width=page.width,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        continer=ft.Container(content=column,bgcolor=ft.colors.BLUE_400)
        
        print(self.marizArbol())
        for i in self.marizArbol():
            row=ft.Row(spacing=30,
                alignment=ft.MainAxisAlignment.CENTER)
            for h in i:  
                if h=="":
                    row.controls.append(self.hacerCuadros("  "))
                row.controls.append(self.hacerCuadros(h))
                
            column.controls.append(row)
        return(continer)

