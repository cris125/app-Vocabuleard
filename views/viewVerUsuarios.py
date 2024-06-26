
from baseDeDatos.dbUsuario import DbUsuario
import flet as ft

class ViewVerUsuarios:
    def __init__(self) -> None:
        self.contenedor=ft.Row(alignment=ft.MainAxisAlignment.CENTER,)
    def consultarUsuarios(self):
        
        db=DbUsuario()
        usuario=db.ver_tabla_usuario()
        account=db.ver_account()
        retur=[(usuario[i][0],usuario[i][1],usuario[i][3],usuario[i][4]) for i in range(len(usuario))]
        return(retur)
        
    def ventanaVerUsuario(self):
        usuarios=self.consultarUsuarios()
        row=[]
        for usuario in usuarios:
            cells=[]
            for datos in usuario:   
                cells.append( ft.DataCell(ft.Text(str(datos))))  
            row.append(ft.DataRow(cells))
            
        txt_number = ft.Text(value="Los Usuarios Son", text_align=ft.TextAlign.CENTER, width=500,size=30)
        
        
        return ft.Column([
            ft.Row([txt_number],alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([
            ft.DataTable(columns=[
                ft.DataColumn(ft.Text("Id")),
                ft.DataColumn(ft.Text("User Name")),
                ft.DataColumn(ft.Text("Acount Id"), numeric=True),
                ft.DataColumn(ft.Text("Promedio Nota")),
            ],rows=row,
            )],alignment=ft.MainAxisAlignment.CENTER,)  
        ],scroll=True)
            