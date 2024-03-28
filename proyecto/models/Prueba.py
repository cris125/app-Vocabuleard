import json
import sqlite3
from baseDeDatos import dbPrueba
class Prueba:
    def __init__(self, nombre) -> None:
        
        last_id=dbPrueba()
        last_id=last_id.get_last_id_prueba()
        if last_id is None:
            self.id = 1  # Si no hay pruebas, establecer el ID como 1
        else:
            self.id = int(last_id) + 1
        self.preguntas = []
        self.nombre = nombre
        self.intentos=0
        self.calificacion=0

    def insertarPregunta(self, pregunta):
        self.preguntas.append(pregunta)

    
    