
import flet as ft
from .viewIniciarSesion import ViewIniciarSesion
from .viewPrincipalAdmin import VentanaPrincipalAdmin
from .viewAgregarPrueba import ViewAgregarPrueba
from .viewAgregarAdministradores import AgregarAdministradores
from .viewEliminarUsuarios import EliminarUsuarios
from .viewVerPruebas import VerPruebas
from .viewEliminarPrueba import EliminarPrueba
from .viewsVentaPrincipalEstudiantes import VentanaPrincipalEstudiante
from .viewVerUsuarios import ViewVerUsuarios
from .viewVerArbolNotas import ArbolNotas
from .viewInterfazUsuario import InterfazUsuario
from .viewVocabulay import Vocabulay
from .viewEje import EjercicioFrase
from .viewProgreso import MostrarProgreso
from .viewCrearUsuario import CrearUsuario
from .viewNotasComunes import NotasComunes
from .viewAnalisisMatematico import AnalisisMat
class VentanaMain:
    def iniciar(self):
       ft.app(target=self.main, view=ft.AppView.WEB_BROWSER)
       """ ft.app(target=self.main)"""
    def route(self,route):
        self.page.views.clear()
       
        self.page.views.append( ft.View(
                "/",[self.interfaz(),self.bienvenida()],
        ))
        
        if  self.page.route == "/pagInicio":
            self.page.views.append(ft.View(
                    "/pagInicio",[self.interfaz(),self.pagInicio()],
        ))
        if  self.page.route == "/crearUsuario":
                        a=CrearUsuario()
                        self.page.views.append(ft.View(
                                "/crearUsuario",[self.interfaz(),a.crearUser(self.page)],
                        ))    
        if self.page.client_storage.get("user") and self.page.client_storage.get("is_admin"):

                if  self.page.route == "/pagInicioAdmin":
                        a=VentanaPrincipalAdmin()
                        
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin",[a.ventanaAdmin(self.page)],
                        )) 

                 

                if  self.page.route == "/pagInicioAdmin/verUsuarios":
                        a=VentanaPrincipalAdmin()
                        h=ViewVerUsuarios()
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/verUsuarios",[a.ventanaAdmin(self.page),h.ventanaVerUsuario()],
                        ))
                
                if  self.page.route == "/pagInicioAdmin/agregarPrueba":
                        a=VentanaPrincipalAdmin()
                        h=ViewAgregarPrueba(self.page)    
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/agregarPrueba",[ft.Column(
                                        [a.ventanaAdmin(self.page), h.prueba()],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))
                if  self.page.route == "/pagInicioAdmin/verPruebas":
                        a=VentanaPrincipalAdmin()
                        h=VerPruebas()   
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/verPruebas",[ft.Column(
                                        [a.ventanaAdmin(self.page), h.pruebas(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))
                if  self.page.route == "/pagInicioAdmin/agregarAdmin":
                        a=VentanaPrincipalAdmin()
                        h=AgregarAdministradores()    
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/agregarAdmin",[ft.Column(
                                        [a.ventanaAdmin(self.page), h.ventanaAgreAdmin(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))
                        
                if  self.page.route == "/pagInicioAdmin/eliminarUsuario":
                        a=VentanaPrincipalAdmin()
                        h=EliminarUsuarios()   
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/eliminarUsuario",[ft.Column(
                                        [a.ventanaAdmin(self.page), h.ventanaEliminarUsuario(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))
                if  self.page.route == "/pagInicioAdmin/eliminarPrueba":
                        a=VentanaPrincipalAdmin()
                        h=EliminarPrueba()   
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/eliminarPrueba",[ft.Column(
                                        [a.ventanaAdmin(self.page), h.ventanaEliminarPrueba(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))

                if  self.page.route == "/pagInicioAdmin/verArbolNotas":
                        a=VentanaPrincipalAdmin()
                        h=ArbolNotas()   
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/verArbolNotas",[ft.Column(
                                        [a.ventanaAdmin(self.page),h.contador(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))
                if  self.page.route == "/pagInicioAdmin/notaComun":
                        a=VentanaPrincipalAdmin()
                        h=NotasComunes()   
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/notaComun",[ft.Column(
                                        [a.ventanaAdmin(self.page),h.graficaNotasComunes(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))
                        
                if  self.page.route == "/pagInicioAdmin/analisisMatematico":
                        a=VentanaPrincipalAdmin()
                        h=AnalisisMat()   
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/analisisMatematico",[ft.Column(
                                        [h.pestañaAnalisis(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))
        if self.page.client_storage.get("user") and (not self.page.client_storage.get("is_admin")):
                if  self.page.route == "/pagEstudioante":
                        a=VentanaPrincipalEstudiante()
                        h=InterfazUsuario()
                        self.page.views.append(ft.View(
                                "/pagEstudioante",[ft.Column(
                                        [h.hacerintefazEstudiantes(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))  
                        
                if  self.page.route == "/pagEstudioante/hacerPrueba":
                        a=VentanaPrincipalEstudiante()
                        h=InterfazUsuario()
                        self.page.views.append(ft.View(
                                "/pagEstudioante/hacerPrueba",[ft.Column(
                                        [a.ventanaEstudiante(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        )) 
                if  self.page.route == "/pagEstudioante/vocabulary":
                        a=Vocabulay()
                        h=InterfazUsuario()
                        self.page.views.append(ft.View(
                                "/pagEstudioante/vocabulary",[ft.Column(
                                        [h.hacerintefazEstudiantes(self.page),a.aprtadoVocabulario(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        )) 
                if  self.page.route == "/pagEstudioante/ejerFrase":
                        a=EjercicioFrase()
                        h=InterfazUsuario()
                        self.page.views.append(ft.View(
                                "/pagEstudioante/ejerFrase",[ft.Column(
                                        [h.hacerintefazEstudiantes(self.page),a.mostrarEjer(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))  
                
               
                if  self.page.route ==  "/pagEstudioante/Verprogreso":
                        a=MostrarProgreso()
                        h=InterfazUsuario()
                        self.page.views.append(ft.View(
                                 "/pagEstudioante/Verprogreso",[ft.Column(
                                        [h.hacerintefazEstudiantes(self.page),a.venPrincipal(self.page)],
                                        scroll=True,  # Habilita la barra de desplazamiento vertical
                                        alignment=ft.alignment.center
                                )],
                        ))  

        if  self.page.route == "/pagInicioUsuarios":
                 self.page.views.append(ft.View(
                                "/pagInicioAdmin",[self.interfaz(),self.pagInicio()],
                        ))    

            
        self.page.update()
    def limpiar(self,page): 
            page.clean()
            page.add(self.interfaz(page))
            
    def pagInicio(self):
            a=ViewIniciarSesion()  
            res=a.pestañaInicio(self.page)
            return(res) 

    def bienvenida(self):
            return(ft.Row([ft.Text(value="Bienvenido de vuelta", text_align=ft.TextAlign.CENTER, width=500,size=30),
                          ],alignment=ft.MainAxisAlignment.CENTER,))

    

    def interfaz(self):    
            controlarInterfaz=ft.Container(ft.Row([
                ft.Container(
                        ft.OutlinedButton(text="Inicio",width=100, on_click=lambda _: self.page.go("/bienvenida") ),
                        width=150,height=50,
                        padding=5,),
                
                ft.Container(
                        ft.OutlinedButton(text="Iniciar sesion",width=100, on_click=lambda _: self.page.go("/pagInicio") ),
                        width=150,height=50,
                        padding=5,),
                        
                ft.Container(
                        ft.OutlinedButton(text="Crear Usuario",width=100, on_click=lambda _: self.page.go("/crearUsuario") ),
                        width=150,height=50,
                        padding=5,),
                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,),bgcolor=ft.colors.SECONDARY_CONTAINER, padding=15)
            
            return controlarInterfaz 
    def view_pop(self,view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        
    def main(self, page: ft.Page): 
        self.page=page  
        page.title = "VocaduLearn"
        page.on_route_change = self.route
        page.on_view_pop = self.view_pop
        page.go(page.route)
 
    
         
    
    
