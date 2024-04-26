import mysql.connector
class Usuario:
    def __init__(self, nombre, admin=False):
        self.nombre = nombre
        self.admin = admin

# Variable global para almacenar información sobre el usuario actual
usuario_actual = None

# Función para establecer el usuario actual
def establecer_usuario_actual(nombre, admin=False):
    global usuario_actual
    usuario_actual = Usuario(nombre, admin)

# Función para verificar si el usuario actual está registrado
def esta_registrado():
    global usuario_actual
    return usuario_actual is not None

# Función para verificar si el usuario actual es un administrador
def es_admin():
    global usuario_actual
    if esta_registrado():
        return usuario_actual.admin
    else:
        return False
def logOut():
    global usuario_actual
    usuario_actual=None
    return False
# Ejemplo de uso:

"""baseDatosConeccion=conexion = mysql.connector.connect(
        host="monorail.proxy.rlwy.net",
        user="root",
        password="VQkGgBYZGwDkSDSoDNBUDKooRxdwJUOJ",
        port="16333",
        database="railway"
    )"""

baseDatosConeccion=conexion = mysql.connector.connect(
        host="monorail.proxy.rlwy.net",
        user="root",
        password="dFmitdJCLqsRvtCtBpvZINZfylIKdOUb",
        port="44693",
        database="railway"
    )
"""establecer_usuario_actual("Usuario1", admin=True)
print("¿Está registrado?", esta_registrado())
print("¿Es admin?", es_admin())"""
