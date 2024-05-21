import numpy as np
import matplotlib.pyplot as plt
import math
import json
import matplotlib.pyplot as plt
import random
import flet as ft
from flet.matplotlib_chart import MatplotlibChart
# Configuración para exportar la gráfica en formato SVG
import matplotlib
matplotlib.use("svg")


class CrearFucion:
    def __init__(self,pendiente,constante) -> None:
        self.pendiente=pendiente
        self.constante=constante
        
    def imagen(self,x):
        return((self.pendiente*x)+self.constante)
    
class CalculoAreaCurva:
    def promedio(self,lista):
        return (sum(lista) / len(lista))


    def hacerPendienteFormula(self,listX, listY):
        promedioX = self.promedio(listX)
        promedioY = self.promedio(listY)
        n = len(listX)

        sumXCuadra=0
        for i in listX:
            sumXCuadra+=i**2

        sumX=sum(listX)

        sumYPorX = 0

        for i in range(len(listX)):
            sumYPorX += (listX[i] * listY[i])

        pendiente = (sumYPorX - n * promedioX * promedioY) / (sumXCuadra - (sumX**2)/n)

        return (pendiente)

    def saberConstante(self,datosX,datosY,pendiente):
        return (sum(datosY)-pendiente*sum(datosX))/len(datosX)

    def hacerFucion(self,datosX,datosY,pendiente):
        newY = [(pendiente * i) + self.saberConstante(datosX,datosY,pendiente) for i in datosX]
        return(newY)

    def hacerGrefico(self,datosX, datosY ,puntosY):
        
        fig = plt.figure(figsize=(4, 3), facecolor='w')

        # Graficar la línea de regresión
        plt.plot(datosX, datosY, '-', label='Línea de Regresión')

        # Graficar los puntos de datos
        plt.scatter(datosX, puntosY, color='red', label='Puntos de Datos')

        # Rellenar el área debajo de la línea
        plt.fill_between(datosX, datosY, facecolor='white', alpha=0.6)

        plt.title("Visualización de Muestra", fontsize=10)
        plt.xlabel("Datos X")
        plt.ylabel("Datos Y")
        plt.legend()

        # Cerrar la figura
        e=ft.Row([ft.Row([MatplotlibChart(fig, expand=True)],width=600)],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
        # Indicar al usuario dónde se guardó la imagen
        return(e)
    def integralDefi(self,funcion,limInf,limSup):
        a = limInf  # Extremo inferior del intervalo
        b = limSup  # Extremo superior del intervalo
        n = 10  # Número de subintervalos (debe ser par para la regla de Simpson)
        h = (b - a) / n  # Ancho de cada subintervalo

        suma = funcion(a) + funcion(b)  # Suma de los extremos
        for i in range(1, n, 2):  # Suma de los términos impares
            suma += 4 * funcion(a + i * h)

        for i in range(2, n-1, 2):  # Suma de los términos pares
            suma += 2 * funcion(a + i * h)

        area = suma * h / 3  # Fórmula de la regla de Simpson

        return area


    def main(self,datosY:list):
        
        datosY=[1,1.3,5,1,2,3,6,9,9]
        datosX = [i for i in range(len(datosY))]
        
        pendiente = self.hacerPendienteFormula(datosX, datosY)
        newY=self.hacerFucion(datosX,datosY,pendiente)
        

        grafico=self.hacerGrefico(datosX, newY,datosY)
        newFuncion=CrearFucion(pendiente,self.saberConstante(datosX,datosY,pendiente))
        
        print(self.integralDefi(newFuncion.imagen,0,max(datosX)))
        return(grafico)


