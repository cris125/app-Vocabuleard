import flet as ft 
from models.ArbolB import Diccionario
class Vocabulay:
    def buscarPalabra(self,e):
        dic=Diccionario()
        diccionario=dic.hacerDiccionario()
        palEn=diccionario.search(self.palabraBusqueda.value)
        if palEn is not None:
            for i in palEn:
                if i != self.palabraBusqueda.value:
                    self.palabraEncontrada.value=i
        else:
             self.palabraEncontrada.value="la Db no tiene esta Traduccion"
        self.page.update()

    def aprtadoVocabulario(self,page):
        self.page=page
        self.palabraBusqueda=ft.TextField(value="(palabra)")
        self.palabraEncontrada=ft.Text(value="",size=25)
        contenedor=ft.Container(
            content=ft.Row(
                [   self.palabraBusqueda,
                    ft.ElevatedButton(text="Buscar Palabra",on_click=self.buscarPalabra),
                    self.palabraEncontrada   
                ], alignment=ft.MainAxisAlignment.CENTER
            ))
        
        return(contenedor)