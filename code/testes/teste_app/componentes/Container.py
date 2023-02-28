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

EconomiaTitle = ContainerTemplate(
            content=ft.Text("Economia", color='#000000'),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,  
            bgcolor='#EBEBF0',          
            width=70,
            height=20,
            border_radius=20,
            )

IconPercentage = ContainerTemplate(
            content=ft.Icon(name=ft.icons.AREA_CHART_OUTLINED, color='#00d154', size=30),
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

Cultura = ContainerTemplate(
                ft.Column(
                    [
                            ft.Row([
                                ft.Icon(name=ft.icons.ENERGY_SAVINGS_LEAF, color='#00d154', size=15), 
                                ft.Text("Cultura", color='#000000', weight=ft.FontWeight.W_600),
                            ]),
                            ft.Text("67", color='#000000', weight=ft.FontWeight.W_600, size=60),
                            ft.Text("mm/dia", color='#000000'),
                    ]
                ),                        
)

Referencia = ContainerTemplate(
                ft.Column(
                    [
                            ft.Row([
                                ft.Icon(name=ft.icons.WATER_DROP, color='#00d154', size=15), 
                                ft.Text("Referência", color='#000000', weight=ft.FontWeight.W_600),
                            ]),
                            ft.Text("48", color='#000000', weight=ft.FontWeight.W_600, size=60),
                            ft.Text("mm/dia", color='#000000'),
                    ]
                )
)

'''content=ft.Icon(name=ft.icons.WATER_DROP, color='#00d154', size=30), '''

'''Referencia = ContainerTemplate(
                ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(name=ft.icons.WATER_DROP, color='#00d154', size=30),
                            title=ft.Text("Referência", color='#000000'),
                            subtitle=ft.Text(
                                "48", color='#000000',
                            ),
                        ),
                    ]
                ),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,  
                bgcolor='#EBEBF0',          
                width=70,
                height=20,
                border_radius=20,
)'''


Evapotranspiracao = ContainerTemplate(
            ft.Row(
                    [
                        Referencia, 
                        Cultura,
                    ]
            ),       
            margin=20,
            padding=20,
            alignment=ft.alignment.center,
            bgcolor='white',
            width=500,
            height=300,
            border_radius=10,        
            )

Economia = ContainerTemplate(
                ft.Row(
                        [
                            EconomiaTitle, 
                            IconPercentage, 
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
          
        