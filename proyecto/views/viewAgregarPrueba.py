import flet as ft

class ViewAgregarPrueba:
    def ventaAgregarPrueba(self,page):
        preguntas = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        def AgregarPregunta(e):
            print(e.control.data[0].value)
            
        def AgregarOtraPregunta(e):
            preguntas.controls.clear()
            page.update()
            
            a=ft.TextField(value="Respuestas A")
            b= ft.TextField(value="Respuestas B")
            c=ft.TextField(value="Respuestas C")
            d=ft.TextField(value="Respuestas D")
            respuestaCorrecta=ft.TextField(value="Respuestas D")
            
            continer=ft.Container(content=ft.Column(
                [           ft.Text(value="Pregunta:",size=20),
                            ft.TextField(value="(pregunta)"),
                            ft.Text(value="Respuestas:"),
                            a, b,c,d,
                            ft.Text(value="Respuesta Correcta:"),
                            respuestaCorrecta,
                            ft.TextButton(text="Agregar Pregunta",data=(a,b,c,d,respuestaCorrecta),on_click=AgregarPregunta)
                 ],scroll=ft.ScrollMode.ALWAYS)
                    ,border=ft.border.all(2, ft.colors.BLACK), border_radius=5,padding=5,width=500)
            preguntas.controls.append(continer)
            page.update()
            
        
        intefaz=ft.Row([ft.TextButton(text="Agregar Otra pregunta", on_click=AgregarOtraPregunta),ft.TextButton(text="Guardar Prueba")],alignment=ft.MainAxisAlignment.CENTER,)
        page.add(intefaz,preguntas)
        
        
