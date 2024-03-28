import json
import mysql.connector
from models.usuario import Usuario
from baseDeDatos.crearTablas import CrearTablas

class dbPrueba:
    conexion = mysql.connector.connect(
        host="monorail.proxy.rlwy.net",
        user="root",
        password="VQkGgBYZGwDkSDSoDNBUDKooRxdwJUOJ",
        port="16333",
        database="railway"
    )

    def guardar_en_base_de_datos(self,prueba):
        try:
            cursor = self.conexion.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pruebas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre TEXT,
                    preguntas TEXT,
                    intentos INT,
                    calificacion INT
                )
            ''')

            # Convertir las preguntas a una cadena JSON antes de guardarlas
            preguntas_json = []
            for pregunta in prueba.preguntas:
                preguntas_json.append({
                    'pregunta': pregunta.pregunta,
                    'respuestas': ', '.join(pregunta.respuestas),
                    'respuestaCorrecta': pregunta.respuestaCorrecta,
                    'imagen': pregunta.imagen,
                })

            # Insertar los datos en la tabla
            cursor.execute('''
                INSERT INTO pruebas (nombre, preguntas, intentos, calificacion)
                VALUES (%s, %s, %s, %s)
            ''', (prueba.nombre, json.dumps(preguntas_json), prueba.intentos, prueba.calificacion))

            self.conexion.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print("Error al guardar en la base de datos:", e)

    def leer_desde_base_de_datos(self, prueba):
        try:
            cursor = self.conexion.cursor()

            cursor.execute('SELECT * FROM pruebas')
            registros = cursor.fetchall()

            for registro in registros:
                print(f"Nombre: {registro[1]}")
                print(f"Id: {registro[0]}")
                print(f"Calificación: {registro[4]}")
                preguntas = json.loads(registro[2])
                for pregunta in preguntas:
                    print(f"Pregunta: {pregunta['pregunta']}")
                    print(f"Respuestas: {pregunta['respuestas']}")
                    print(f"Respuesta correcta: {pregunta['respuestaCorrecta']}")
                    print(f"Imagen: {pregunta['imagen']}")
                    print("-" * 30)

            cursor.close()
        except mysql.connector.Error as e:
            print("Error al leer desde la base de datos:", e)

    def get_last_id_prueba(self):
        last_id = 0
        try:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT MAX(id) FROM pruebas')
            last_id = cursor.fetchone()[0]
        except mysql.connector.Error as e:
            print("Error al obtener el último ID de prueba:", e)
        finally:
            if cursor:
                cursor.close()
        return last_id
