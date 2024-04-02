import json
import sqlite3
from baseDeDatos.dbPrueba import dbPrueba
class Prueba:
    def __init__(self) -> None:
        
        a=dbPrueba()
        last_id=a.get_last_id_prueba()
        if last_id is None:
            self.id = 1  # Si no hay pruebas, establecer el ID como 1
        else:
            self.id = int(last_id) + 1
        self.preguntas = []
        self.nombre = None
        self.intentos=0
        self.calificacion=0

    def setNombre(self,nombre):
        self.nombre=nombre
    def insertarPregunta(self, pregunta):
        self.preguntas.append(pregunta)

    
    