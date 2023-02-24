import flet as ft
from flet import UserControl

class ContainerTemplate(UserControl):
    def __init__(
        self, 
        content=ft.Text("Non clickable"),
        margin=None,
        padding=None,
        alignment=None,
        bgcolor=None,
        width=None,
        height=None,
        border_radius=None
    ):

        # Metodo init
        super().__init__()
        self.content=content
        self.margin=margin
        self.content=content
        self.margin=margin
        self.padding=padding
        self.alignment=alignment
        self.bgcolor=bgcolor
        self.border_radius=border_radius 



    def build(self):
        return ft.Container(
            content=self.content,
            margin=self.margin,
            padding=self.padding,
            alignment=self.alignment,
            bgcolor=self.bgcolor,
            width=self.width,
            height=self.height,
            border_radius=self.border_radius,
        )

IrrigacaoTitle = ContainerTemplate(
            content=ft.Text("Irrigação", color='#000000'),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,  
            bgcolor='#EBEBF0',          
            width=70,
            height=20,
            border_radius=20,
            )

IconTime = ContainerTemplate(
            content=ft.Icon(name=ft.icons.WATCH_LATER, color='#00d154', size=30),
            )

Irrigacao = ContainerTemplate(
            ft.Row(
                        [
                            IrrigacaoTitle, 
                            IconTime, 
                        ]
                    ),
                    
            margin=50,
            padding=50,
            alignment=ft.alignment.center,
            bgcolor='white',
            width=150,
            height=150,
            border_radius=10,
            )

Evapotranspiracao = ContainerTemplate(
                content=ft.Text("Non clickable"),
                bgcolor='white',
            )

Economia = ContainerTemplate(
                content=ft.Text("Non clickable"),
                alignment=ft.alignment.center,
                bgcolor='white',
            )
          
        