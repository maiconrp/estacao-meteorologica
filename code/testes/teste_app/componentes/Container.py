import flet as ft
from flet import *
from flet import TextField, TextAlign
from componentes.NavigationBar import navigation_bar

"""page_container = Row(
    controls=[
        content=Column(
            controls=[

            ]
        )
    ]
)"""




class TextTemplate:
    """
    Classe para criar campos de texto com configurações comuns

    Atributos:
        ATRIBUTO    TIPO        DEFINIÇÃO                               DEFAULT
        label       (str)       Descrição do campo de texto             ("Texto")
        value       (int)       Valor inicial do campo de texto         (0)
        text_align  (TextAlign) Alinhamento do texto dentro do campo    (TextAlign.CENTER)
        width       (int)       Largura do campo de texto               (175)
        suffix_text (str)       Texto que aparece após o valor          ("")
    """

    def __init__(self, bgcolor='white', value='Milho', width=200, height=20, margin = 0, color='#000000', size=10, weight=FontWeight.W_600):
        self.bgcolor = bgcolor
        self.value = value
        self.width = width
        self.height = height
        self.margin = margin
        self.color = color
        self.size = size
        self.weight = weight

    def build(self):
        """
        Cria um objeto TextField com as configurações especificadas no construtor

        Retorna: TextField: campo de texto criado
        """
        return Text(
            bgcolor=self.bgcolor,
            value=self.value,
            width=self.width,
            height=self.height,
           # margin = self.margin,
            color = self.color,
            size = self.size,
            weight = self.weight
        )


# Criação de campos de texto com configurações comuns


cultura = TextTemplate(
    value="Milho",
    size=22,
    weight=FontWeight.W_700, 
    height=35,            
).build()

plantio = TextTemplate(
    value="Plantio: 25/08/2022",         
).build()

area = TextTemplate(
    value="Área: 5000m²",            
).build()

estagio = TextTemplate(
    value="Estágio: Maturação",          
).build()

card_cultura = Container(
    bgcolor = 'white',
    height=95,
    width=300,
    border_radius = 15,
    padding = padding.only(top=15, left=20, right=20, bottom=25),
    margin = margin.only(top=10),
    content = Row(
        controls=[
            Container(
                Icon(icons.ENERGY_SAVINGS_LEAF_ROUNDED, color='#00D154', size=56)
            ),
            Column(
                controls=[
                    cultura,
                    plantio,
                    area,
                    estagio,
                ]
            ),
        ]
    ),
)

line = Container(
        width=290,
        height=1,
        bgcolor='#00D154',
        margin = margin.only(left=5, bottom=10)
    )

relatorio = Container(
    Row(
        controls=[
            Icon(icons.CIRCLE_ROUNDED, color='#00D154', size=16),
            Text(value='Relatório', color='#000000', size=20, weight=FontWeight.W_600)          
        ]
    )
)

card_irrigacao = Container(
    content=Row(alignment='spaceBetween',
        controls=[
            Container(
                bgcolor = 'white',
                height=140,
                width=140,
                border_radius = 15,
                padding = padding.only(top=14, left=17, right=17, bottom=22),
                margin = margin.only(top=7),
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Container(
                                    bgcolor = '#EBEBF0',
                                    height=24,
                                    width=75,
                                    border_radius = 20,  
                                    margin = margin.only(right=7),                              
                                    content = ft.Text('Irrigação', color='#000000', size=12, weight=FontWeight.W_700), 
                                ),
                                Icon(name='settings', color='#00D154', size=16),
                            ]
                        ),
                        Container(                           
                            Text(value='1h30', color='#000000', size=39, weight=FontWeight.W_700),
                            margin = margin.only(top=-10)
                        ), 
                        Container(
                            Text(value='Tempo ideal de irrigação para hoje', color='#000000', size=11, weight=FontWeight.W_400)
                        ), 
                    ]
                ),
            ),
            Container(
                bgcolor = 'white',
                height=140,
                width=140,
                border_radius = 15,
                padding = padding.only(top=14, left=17, right=17, bottom=22),
                margin = margin.only(top=7),
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Container(                   
                                    bgcolor = '#EBEBF0',
                                    height=24,
                                    width=75,
                                    border_radius = 20,  
                                     margin = margin.only(right=7), 
                                    content = ft.Text('Economia', color='#000000', size=12, weight=FontWeight.W_700) 
                                                                                                      
                                ),

                                Icon(name='settings', color='#00D154', size=16),
                            ]
                        ),
                        Container(
                            Text(value='27%', color='#000000', size=39, weight=FontWeight.W_700),
                            margin = margin.only(top=-10)
                        ), 
                        Container(
                            Text(value='760 litros', color='#000000', size=11, weight=FontWeight.W_400),
                            Text(value='economizados', color='#000000', size=11, weight=FontWeight.W_400)
                        ), 
                    ]
                ),
            ),
        ]
    )
)

card_ET = Container(
    bgcolor = 'white',
    height=120,
    width=300,
    border_radius = 15,
    padding = padding.only(top=25, left=20, right=20, bottom=25),
    margin = margin.only(top=15, bottom=12),
)

page_container = Container(
    content=Column(
        controls=[
            Row(alignment='spaceBetween',
                controls=[
                    Container(
                        Text(value='Olá, Victor', color='#000000', size=25, weight=FontWeight.W_700)
                    ), 
                    
                    Row(
                        controls=[
                            Text(value='Estação', color='#000000', size=13),
                            Icon(name='settings', color='#00D154', size=16)
                        ]
                    )                                            
                ]
            ),
            Container(
                        Text(value='Quinta, 26 de janeiro', color='#000000', size=11),
                        margin = margin.only(top=-11)
                    ), 
            Container(
                content=card_cultura,
            ),
            Container(
                content=line,
            ),
            Container(
                content=relatorio,
            ),
            Container(
                content=card_irrigacao,
            ), 
            Container(
                content=card_ET,
            ),
            navigation_bar
        ]
    )
)


container_home = Container(
    width=350,
    height=650,
    bgcolor='#EFEFEF',
    border_radius=35,
    padding = padding.only(top=20, left=23, right=23, bottom=0),
    content=page_container
)















container_cultura = Container(

)