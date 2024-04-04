
import flet as ft
from .viewIniciarSesion import ViewIniciarSesion
from .viewPrincipalAdmin import VentanaPrincipalAdmin
from .viewAgregarPrueba import ViewAgregarPrueba
from .viewAgregarAdministradores import AgregarAdministradores
from .viewEliminarUsuarios import EliminarUsuarios
import variableGlobal

class VentanaMain:
    def iniciar(self):
        """ft.app(target=self.main, view=ft.AppView.WEB_BROWSER)"""
        ft.app(target=self.main)
        ft.app()
        
    def route(self,route):
        self.page.views.clear()
       
        self.page.views.append( ft.View(
                "/",[self.interfaz(),self.bienvenida()],
        ))
        
        if  self.page.route == "/pagInicio":
            self.page.views.append(ft.View(
                    "/pagInicio",[self.interfaz(),self.pagInicio()],
        ))
            
        if variableGlobal.esta_registrado() and variableGlobal.es_admin():

                if  self.page.route == "/pagInicioAdmin":
                        a=VentanaPrincipalAdmin()
                        
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin",[a.ventanaAdmin(self.page)],
                        )) 
                if  self.page.route == "/pagInicioAdmin/verUsuarios":
                        a=VentanaPrincipalAdmin()
                        
                        self.page.views.append(ft.View(
                                "/pagInicioAdmin/verUsuarios",[a.ventanaAdmin(self.page),a.pagUsuarios()],
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
            return(ft.Row([ft.Text(value="Bienvenido de vuelta", text_align=ft.TextAlign.CENTER, width=500,size=30)],alignment=ft.MainAxisAlignment.CENTER,))

    

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
 
    
         
    
    
