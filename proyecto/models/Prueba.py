from .Pregunta import Pregunta
class Prueba:
    def __init__(self,nombre) -> None:
        self.preguntas=[]
        self.nombre=nombre
    def insertarPregunta(self,pregunta):
        self.preguntas.append(pregunta)
    
    def hacerCuestionario(self):  
        for i in self.preguntas:
            print (i.pregunta)
            print(i.respuestas)
            T=input()
            if T==i.respuestaCorrecta:
                print("bien")
            else:
                print("mal")