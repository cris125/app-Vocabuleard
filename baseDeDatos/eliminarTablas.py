import mysql.connector
import variableGlobal

class ElimTablas:
    conexion = variableGlobal.baseDatosConeccion
    
    def __init__(self):
        self.cursor = self.conexion.cursor()

    def drop_table_pruebas(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS pruebas")
            print("La tabla usuarios ha sido eliminada correctamente")
        except mysql.connector.Error as e:
            print("Error al eliminar la tabla de usuarios:", e)
    
    def drop_table_usuario(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS usuarios")
            print("La tabla usuarios ha sido eliminada correctamente")
        except mysql.connector.Error as e:
            print("Error al eliminar la tabla de usuarios:", e)

    def drop_table_account(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS account")
            print("La tabla account ha sido eliminada correctamente")
        except mysql.connector.Error as e:
            print("Error al eliminar la tabla de account:", e)
            
    def close_connection(self):
        try:
            self.cursor.close()
            self.conexion.close()
            print("Conexión cerrada correctamente")
        except mysql.connector.Error as e:
            print("Error al cerrar la conexión:", e)