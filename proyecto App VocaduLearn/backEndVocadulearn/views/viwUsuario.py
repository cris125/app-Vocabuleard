import sqlite3

from usuario import Usuario
from crearTablas import CrearTablas


class ViwUsuario:
    def crearUsuario(self,user:str):
        CrearTablas.create_table_account()
        CrearTablas.create_table_usuario()
        newUser=Usuario(user)
        self.insert_usuario(newUser)

    def insert_usuario(self,usuario):
        self.insert_account(usuario)
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO usuarios (id, userName,id_account)
            VALUES (?, ?, ?)
        ''', (usuario.id, usuario.userName,usuario.id_account))
        connection.commit()
        connection.close()

    def insert_account(self,usuario:Usuario):
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO account (
                id, 
                prueba,
                activate)
            VALUES (?, ?,?)
        ''', (usuario.id_account, usuario.account.prueba,usuario.account.activate))
        connection.commit()
        connection.close()
            
    def ver_tabla_usuario(self):
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        # Define la estructura de la tabla
        cursor.execute('''
            SELECT * FROM  usuarios; 
        ''')
        usuarios = cursor.fetchall()
        connection.close()
        return(usuarios)
    
    def ver_tabla_account(self,id):
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        # Define la estructura de la tabla
        cursor.execute('''
            SELECT * FROM  account WHERE id = ?; 
        ''',(id,))
        usuarios = cursor.fetchall()
        connection.close()
        return(usuarios)
    
    def ver_account(self):
        connection = sqlite3.connect('sql3.db')
        cursor = connection.cursor()
        # Define la estructura de la tabla
        cursor.execute('''
            SELECT * FROM  account; 
        ''')
        usuarios = cursor.fetchall()
        connection.close()
        return(usuarios)
# Ejemplo de uso
xd=ViwUsuario()
pepe=Usuario("pe1")
xd.insert_usuario(pepe)
for i in xd.ver_tabla_usuario():
    txt=[]
    for x in range (len(i)):
        if x==2:
            txt.append(xd.ver_tabla_account(i[x]))
        else:

            txt.append(i[x])
    print(txt)
    

