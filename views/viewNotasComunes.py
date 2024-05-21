import matplotlib.pyplot as plt
from models.ArbolNotasComunes import ArbolNotasComunes
import random
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

# Configuración para exportar la gráfica en formato SVG
import matplotlib
matplotlib.use("svg")

class NotasComunes:
    
    def graficaNotasComunes(self,page: ft.Page):
        fig, ax = plt.subplots()
        a = ArbolNotasComunes()

        # Insertar 50 valores aleatorios en el árbol
        for i in range(1000):
            a.insertar(random.randrange(0, 11))

        # Obtener los datos en orden
        xd = a.inOrden()
        x = [i["valor"] for i in xd]
        y = [i["suma"] for i in xd]

        # Crear la gráfica de barras con colores personalizados
        color_map = plt.get_cmap("RdYlGn")  # Mapa de colores de rojo a verde
    # Mapa de colores de rojo a verde
        norm = plt.Normalize(vmin=0, vmax=10)  # Normalización de valores

        bars = ax.bar(x, y, color=color_map(norm(x)))

        # Asegurarse de que el eje X muestre todos los números del 1 al 10
        ax.set_xticks(range(11))  # Establecer los ticks del eje X
        ax.set_xticklabels(range(11))  # Etiquetas para los ticks

        ax.set_ylabel("Cantidad Notas Repetidas")
        ax.set_title("Gráfica de notas más comunes")

        e=ft.Row([ft.Row([MatplotlibChart(fig, expand=True)],width=800)],alignment=ft.MainAxisAlignment.SPACE_EVENLY,)
        
        # Agregar la gráfica al reporte
        return(e)

