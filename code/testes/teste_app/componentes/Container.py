import flet as ft
from flet import *
from flet import TextField, TextAlign
from componentes.NavigationBar import navigation_bar

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
            color = self.color,
            size = self.size,
            weight = self.weight
        )

# Criação de campos de texto com configurações comuns

card_cultura = Container(
    bgcolor = 'white',
    height=95,
    width=300,
    border_radius = 11,
    #margin = margin.only(top=10),
    padding = padding.only(left=20),
    content = Row(vertical_alignment = CrossAxisAlignment.CENTER,
        controls=[
            Container(
                Image(
                    src=f"/icons/corn.png",
                    width=300,
                    height=300,
                ),  
                margin = margin.only(left=-60, right=-180),
            ),
            Column(alignment = MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        Text('Milho', color='#000000', size=17, weight=FontWeight.W_600),
                        margin = margin.only(bottom=-14)
                    ),
                    Text('Plantio: 255/08/2022 \nÁrea: 5000m² \nEstágio: Maturação', color='#000000', size=10, weight=FontWeight.W_600)  
                ]
            ),
        ]
    ),
)

line = Container(
        width=290,
        height=1.6,
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
    Container(
        bgcolor = 'white',
        height=140,
        width=140,
        border_radius = 11,
        padding = padding.only(top=14, left=17, right=17, bottom=22),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            bgcolor = '#EBEBF0',
                            height=24,
                            width=75,
                            border_radius = 20,  
                            alignment = alignment.center,
                            margin = margin.only(right=7),                              
                            content = ft.Text('Irrigação', color='#000000', size=12, weight=FontWeight.W_700), 
                        ),
                        Image(
                            src=f"/icons/watch.svg",
                            width=20,
                            height=20,
                        ), 
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
)

card_economia = Container(
    Container(
                bgcolor = 'white',
                height=140,
                width=140,
                border_radius = 11,
                padding = padding.only(top=14, left=17, right=17, bottom=22),
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Container(                   
                                    bgcolor = '#EBEBF0',
                                    height=24,
                                    width=75,
                                    border_radius = 20, 
                                    alignment = alignment.center, 
                                    margin = margin.only(right=7), 
                                    content = ft.Text('Economia', color='#000000', size=12, weight=FontWeight.W_700) 
                                                                                                      
                                ),
                                Image(
                                    src=f"/icons/percentage.svg",
                                    width=20,
                                    height=20,
                                ), 
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
)

card_ET = Container(
    bgcolor = 'white',
    height=120,
    width=300,
    border_radius = 11,
    padding = padding.only(top=14, left=20, right=10, bottom=25),
    content=Row(
        controls = [
            Container(
                bgcolor = '#EBEBF0',
                height=120,
                width=22,
                border_radius = 17,
                margin=margin.only(top=-10, bottom=-22, left=-14, right=20)
            ),
            Row(spacing=32,
                controls=[
                    Column(horizontal_alignment = CrossAxisAlignment.CENTER,
                        controls = [
                            Row(alignment = MainAxisAlignment.CENTER,
                                controls=[
                                    Image(
                                        src=f"/icons/gotinha.svg",
                                        width=16,
                                        height=16,
                                    ), 
                                    Container(                   
                                        content = ft.Text('Referencia', color='#000000', size=12, weight=FontWeight.W_700),
                                        margin=margin.only(left=-9),
                                        alignment = alignment.center,
                                    ),
                                ]
                            ),
                            Container(
                                Text(value='48', font_family="Montserrat", color='#000000', size=50, weight=FontWeight.W_700),
                                margin = margin.only(top=-18)
                            ), 
                            Container(
                                Text(value='mm/dia', color='#808080', size=17, weight=FontWeight.W_700), 
                                margin = margin.only(top=-22) 
                            ), 
                        ]
                    ),
                    Column(horizontal_alignment = CrossAxisAlignment.CENTER,
                        controls = [
                            Row(alignment = MainAxisAlignment.CENTER,
                                controls=[
                                    Image(
                                        src=f"/icons/plantinha.svg",
                                        width=16,
                                        height=16,
                                    ), 
                                    Container(                   
                                        content = ft.Text('Cultura', color='#000000', size=12, weight=FontWeight.W_700),
                                        margin=margin.only(left=-9),
                                        alignment = alignment.center,                                                                     
                                    ),
                                ]
                                ),
                            Container(
                                Text(value='48', font_family="Montserrat", color='#000000', size=50, weight=FontWeight.W_700),
                                margin = margin.only(top=-18)
                            ), 
                            Container(
                                Text(value='mm/dia', color='#808080', size=17, weight=FontWeight.W_700), 
                                margin = margin.only(top=-22) 
                            ), 
                        ]
                    ) 
                ]
            )
        ]
    )
)

home_page_container = Container(
    content=Column(
        controls=[
            Row(alignment='spaceBetween',
                controls=[
                    Container(
                        Text(value='Olá, Victor', color='#000000', size=25, weight=FontWeight.W_700)
                    ), 
                    Container(
                        bgcolor = '#EBEBF0',
                        height=31,
                        width=91,
                        border_radius = 20, 
                        content=Row(alignment = MainAxisAlignment.CENTER,
                            controls=[
                                ElevatedButton("Estação", icon=Icon(name='settings', color='#00D154', size=16)),     
                            ]
                        )   
                    ),                                         
                ]
            ),
            Container(
                        Text(value='Quinta, 26 de janeiro', color='#000000', size=11),
                        margin = margin.only(top=-11)
                    ), 
            Card(
                content=card_cultura,  
                elevation=4,           
            ),
            line,
            relatorio,
            Row(
                controls=[
                    Card(
                        card_irrigacao,
                        elevation=6
                    ),
                    Card(
                        card_economia,
                        elevation=6
                    ),
                ]
            ),
            Card(
                card_ET,
                elevation=6
            ),
            navigation_bar
        ]
    )
)

container_home = Container(
    width=350,
    height=650,
    bgcolor='#F7F7FD',
    border_radius=35,
    padding = padding.only(top=20, left=23, right=23, bottom=0),
    content=home_page_container
)

cultura_page = Container(
    content = Column(
        controls = [
            navigation_bar,
        ]
    )
)

container_cultura = Container(
    width=350,
    height=650,
    bgcolor='#EFEFEF',
    border_radius=35,
    padding = padding.only(top=20, left=23, right=23, bottom=0),
    content=cultura_page
)