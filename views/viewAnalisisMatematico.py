import flet as ft
from baseDeDatos.dbUsuario import DbUsuario
from views.viewCalculoFuncionArea import CalculoAreaCurva
import json
class AnalisisMat:
        
    def pestañaAnalisis(self,page:ft.Page):
        self.page=page
        self.page.scroll=True
        self.coneten=ft.Column(scroll=True,height=600)
        self.graf=ft.Row()
        btnNotaGen=ft.ElevatedButton(text="notas generales Segun prueba" ,on_click=self.notasGeneralesEstudaintesGraf)
        self.txtFilNotasGen=ft.TextField(value="Physics 5")
        
        btnNotaEstudiante=ft.ElevatedButton(text="notas todas las pruebas estudiante" ,on_click=self.notasEstuduanteEstudaintesGraf)
        self.txtFilNotasEstudiante=ft.TextField(value="jorge valderrama")
        

        btnNotaEstudiantePrueba=ft.ElevatedButton(text="notas Segun prueba Estuduante" ,on_click=self.notasDeUnaSolaPruebaGraf)
        self.txtFilNotasUsuario=ft.TextField(value="jorge valderrama")
        self.txtFilNotasPrueba=ft.TextField(value="Physics 5")
        
        self.coneten.controls.extend([
                ft.Row([
                    ft.Column([btnNotaGen,self.txtFilNotasGen])
                ,ft.Column([btnNotaEstudiante,self.txtFilNotasEstudiante]),
                 ft.Column([btnNotaEstudiantePrueba,self.txtFilNotasUsuario,self.txtFilNotasPrueba]),
                ]),
                self.graf
        ]
            )
        
        
        return(self.coneten)
    
    def notasGeneralesEstudaintesGraf(self,e):
        a=CalculoAreaCurva()
        notas=self.notasGeneralesEstudaintes(self.txtFilNotasGen.value)
        self.graf.controls.clear()
            
        self.graf.controls.append(a.main(notas))
        self.page.update()
        
    def notasGeneralesEstudaintes(self,prueba="Physics 5"):
        account=DbUsuario().ver_account()
        notas=[json.loads(i[1]) for i in account if i[1] != None]
        notasPro={}

        for i in notas:
            for y in i.keys():
                if y ==prueba:
                    if y in notasPro:
                        notasPro[y].append(sum(i[y])/len(i[y]))
                    else:
                        notasPro.update({y:[sum(i[y])/len(i[y])]})
        return(list(notasPro.values())[0])
    
    
    def notasEstuduanteEstudaintesGraf(self,e):
        a=CalculoAreaCurva()
        notas=self.notasPromedioPruebaSegunEstudiante(self.txtFilNotasEstudiante.value)
        self.graf.controls.clear()
        self.graf.controls.append(a.main(notas[1]))
        self.page.update()

    def notasPromedioPruebaSegunEstudiante(self,estudianteConsultado="daniel hidalgo"):
        usuario=DbUsuario().getUser(estudianteConsultado)
        try:
            notas=json.loads(usuario[3][0][1]) if usuario[3][0][1] != None else None 
        except:
            print("xd")
            return([0],[0])
        for i in notas.keys():
            if len(notas[i])>=2:
                notas[i]=int(sum(notas[i])/len(notas[i]))
            else:
                notas[i]=notas[i][0]
        return(list(notas.keys()),list(notas.values()))
     
     
    def notasDeUnaSolaPruebaGraf(self,e):
        a=CalculoAreaCurva()
        notas=self.notasDeUnaSolaPrueba(self.txtFilNotasUsuario.value,self.txtFilNotasPrueba.value)
        self.graf.controls.clear()
        self.graf.controls.append(a.main(notas))
        self.page.update()    
        
    def notasDeUnaSolaPrueba(self,user="frank Gurrero",prueba="Physics quiz"):    
        usuario=DbUsuario().getUser(user)
        pruebaConsulta=prueba
        notas=json.loads(usuario[3][0][1]) if usuario[3][0][1] != None else None 
        for i in notas.keys():
            if i==pruebaConsulta:
                return(notas[i])
                
                
                
    def __init__(self) -> None:
        pass

    