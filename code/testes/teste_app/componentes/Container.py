import math
from flet import (
    ButtonStyle,
    CircleBorder,
    Card,
    Column,
    Container,
    ContainerTapEvent,
    CrossAxisAlignment,
    ElevatedButton,
    FontWeight,
    Icon,
    Image,
    MainAxisAlignment,
    Row,
    Text,
    alignment,
    border,
    colors,
    icons,
    IconButton,
    margin,
    padding,
    Rotate,
    UserControl,
)

import assets.colors


class TextTemplate(UserControl):
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

    def __init__(
        self,
        bgcolor=assets.colors.BRANCO,
        value="Milho",
        width=200,
        height=20,
        margin=0,
        color="#000000",
        size=10,
        weight=FontWeight.W_600,
    ):
        super().__init__()
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
            color=self.color,
            size=self.size,
            weight=self.weight,
        )


def click(e: ContainerTapEvent):
    print("clck")


card_cultura = Card(
    content=Container(
        bgcolor=assets.colors.BRANCO,
        height=95,
        width=300,
        border_radius=11,
        padding=padding.only(left=20),
        content=Row(
            controls=[
                Container(
                    content=Image(
                        src=f"assets/icons/corn.png",
                        width=300,
                        height=300,
                    ),
                    on_click=click,
                    margin=margin.only(left=-60, right=-180),
                ),
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=0.5,
                    controls=[
                        Text(
                            "Milho",
                            color="#000000",
                            size=17,
                            weight=FontWeight.W_600,
                        ),
                        Text(
                            "Plantio: 25/08/2022",
                            color="#000000",
                            size=10,
                            weight=FontWeight.W_600,
                        ),
                        Text(
                            "Área: 5000m²",
                            color="#000000",
                            size=10,
                            weight=FontWeight.W_600,
                        ),
                        Text(
                            "Estágio: Maturação",
                            color="#000000",
                            size=10,
                            weight=FontWeight.W_600,
                        ),
                    ],
                ),
            ],
        ),
    ),
    elevation=6,
)
line = Container(width=290, height=1.6, bgcolor="#00D154", alignment=alignment.center)

# Criação de campos de texto com configurações comuns

relatorio = Container(
    content=Row(
        controls=[
            Icon(icons.SQUARE, color="#00D154", size=16),
            Text(value="Relatório", color="#000000", size=20, weight=FontWeight.W_600),
        ],
        vertical_alignment=CrossAxisAlignment.CENTER
        # expand=1,
    ),
    width=300,
)

card_irrigacao = Container(
    bgcolor=assets.colors.BRANCO,
    height=140,
    width=140,
    border_radius=11,
    padding=padding.only(top=14, left=17, right=17, bottom=22),
    content=Column(
        spacing=1.5,
        controls=[
            Row(
                spacing=20,
                controls=[
                    Container(
                        bgcolor=assets.colors.WIDGET,
                        height=24,
                        width=75,
                        border_radius=20,
                        alignment=alignment.center,
                        content=Text(
                            "Irrigação",
                            color="#000000",
                            size=12,
                            weight=FontWeight.W_700,
                        ),
                    ),
                    Image(
                        src=f"assets/icons/watch.svg",
                        width=20,
                        height=20,
                    ),
                ],
            ),
            Container(
                Text(value="1h30", color="#000000", size=39, weight=FontWeight.W_700),
            ),
            Container(
                Text(
                    value="Tempo ideal de irrigação para hoje",
                    color="#000000",
                    size=11,
                    weight=FontWeight.W_400,
                )
            ),
        ],
    ),
)

card_economia = Container(
    Container(
        bgcolor=assets.colors.BRANCO,
        height=140,
        width=140,
        border_radius=11,
        padding=padding.only(top=14, left=17, right=17, bottom=22),
        content=Column(
            spacing=1.5,
            controls=[
                Row(
                    spacing=20,
                    controls=[
                        Container(
                            bgcolor=assets.colors.WIDGET,
                            height=24,
                            width=75,
                            border_radius=20,
                            alignment=alignment.center,
                            content=Text(
                                "Economia",
                                color="#000000",
                                size=12,
                                weight=FontWeight.W_700,
                            ),
                        ),
                        Image(
                            src=f"assets/icons/percentage.svg",
                            width=20,
                            height=20,
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Container(
                    Text(
                        value="27%", color="#000000", size=39, weight=FontWeight.W_700
                    ),
                ),
                Container(
                    Text(
                        value="760 litros\neconomizados",
                        color="#000000",
                        size=11,
                        weight=FontWeight.W_400,
                    ),
                ),
            ],
        ),
    ),
)

card_ET = Container(
    bgcolor=assets.colors.BRANCO,
    # height=120,
    width=300,
    border_radius=11,
    padding=padding.only(top=14, left=20, right=10, bottom=25),
    content=Column(
        spacing=12,
        controls=[
            Container(
                bgcolor=assets.colors.WIDGET,
                height=22,
                width=500,
                border_radius=17,
                alignment=alignment.center,
                # margin=margin.only(top=-10, bottom=-22, left=-14, right=20),
                content=Text(
                    "Evapotranspiração",
                    color="#000000",
                    size=12,
                    weight=FontWeight.W_700,
                ),
            ),
            Row(
                spacing=50,
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=1,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Image(
                                        src=f"assets/icons/gotinha.svg",
                                        width=16,
                                        height=16,
                                    ),
                                    Container(
                                        content=Text(
                                            "Referencia",
                                            color="#000000",
                                            size=12,
                                            weight=FontWeight.W_700,
                                        ),
                                        alignment=alignment.center,
                                    ),
                                ],
                            ),
                            Container(
                                Column(
                                    [
                                        Text(
                                            value="48",
                                            font_family="Montserrat",
                                            color="#000000",
                                            size=50,
                                            weight=FontWeight.W_700,
                                        ),
                                        Text(
                                            value="mm/dia",
                                            color="#808080",
                                            size=17,
                                            weight=FontWeight.W_700,
                                        ),
                                    ],
                                )
                            ),
                        ],
                    ),
                    Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=1,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Image(
                                        src=f"assets/icons/plantinha.svg",
                                        width=16,
                                        # height=16,
                                    ),
                                    Container(
                                        content=Text(
                                            "Cultura",
                                            color="#000000",
                                            size=12,
                                            weight=FontWeight.W_700,
                                        ),
                                        alignment=alignment.center,
                                    ),
                                ],
                            ),
                            Container(
                                Text(
                                    value="48",
                                    font_family="Montserrat",
                                    color="#000000",
                                    size=50,
                                    weight=FontWeight.W_700,
                                ),
                            ),
                            Container(
                                Text(
                                    value="mm/dia",
                                    color="#808080",
                                    size=17,
                                    weight=FontWeight.W_700,
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ),
)
