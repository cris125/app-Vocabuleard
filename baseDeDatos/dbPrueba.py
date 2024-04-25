import json
import mysql.connector
from models.usuario import Usuario
from baseDeDatos.crearTablas import CrearTablas
import variableGlobal
class dbPrueba:
    conexion = variableGlobal.baseDatosConeccion

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

    def leer_desde_base_de_datos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT * FROM pruebas')
            registros = cursor.fetchall()
            prueba=[]
            for registro in registros:
                preguntas = json.loads(registro[2])        
                prueba.append((registro[0],registro[1],preguntas,registro[3],registro[4]))
            cursor.close()
            return(prueba)
        except mysql.connector.Error as e:
            print("Error al leer desde la base de datos:", e)
            
    
                        
    def eliminar_prueba(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('DELETE FROM pruebas WHERE id = %s', (id,))
            self.conexion.commit()  # Confirmar los cambios
        except mysql.connector.Error as e:
            print("Error al eliminar desde la base de datos:", e)
        finally:
            if cursor:
                cursor.close()
            
    def verificar_prueba(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM pruebas WHERE id = %s", (id,))
            resultado = cursor.fetchone()
            return resultado[0] > 0
        except mysql.connector.Error as e:
            print(f"Error al verificar usuario: {e}")
            return False
        finally:
            if cursor:
                cursor.close()       
            
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
