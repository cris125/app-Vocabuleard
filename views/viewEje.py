from models.grafoFrase import FraseGrafo
import flet as ft
class EjercicioFrase:
       

    def validarPal(self,e):
        
        if  self.contenido.controls[-1].value in  self.palabras:
                lista=self.crearDropdown(self.grafoFrase .obtener_relaciones([ self.contenido.controls[-1].value,""]))
                self.contenido.controls.append(lista)
        self.page.update()    

    def crearDropdown(self,lista):
        
        if type(lista)==str:
            dd = ft.Dropdown(
                width=150,
                options=[ft.dropdown.Option(lista)],
            )
        else:
                  
            opti=[ft.dropdown.Option(i) for i in lista]
            dd = ft.Dropdown(
                width=150,
                options=opti,
            )
        
        return dd
    

    def mostrarEjer(self,page):
        self.page=page

        self.contenido=ft.Row()
        sumit=ft.ElevatedButton(text="sumit",on_click=self.validarPal)
        contBoton=ft.Row([sumit])

        fraseGrafo=FraseGrafo()

        columnas = fraseGrafo.columnas
        self.grafoFrase = fraseGrafo.hacerGrafo()
        frase = fraseGrafo.hacerFrase()
        fraseEspa=[i[1] for i in frase]
        fraseEspa="Pon la traduccion la siguiente frase en ingles: \n"+str(fraseEspa)

        container=ft.Container(content=ft.Column([
            ft.Text(value=fraseEspa),
             self.contenido,contBoton
        ]))

        self.palabras=[x for i in frase for x in i]
        
        lista=self.crearDropdown(frase[0][0])
        
        self.contenido.controls.append(lista)

        return(container)
    
        


