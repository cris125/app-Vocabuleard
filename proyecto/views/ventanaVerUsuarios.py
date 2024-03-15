from baseDeDatos.dbUsuario import DbUsuario
import flet as ft
from .viewMain import VentanaMain
class VentanaVerUsuarios:
    def __init__(self):
        ft.app(target=self.main)
          
    def main(self,page: ft.Page):
        page.title = "ver Usuarios"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        a=VentanaMain()
        res=a.main()
        page.add(res)
    
