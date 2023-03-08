from flet import (
    Card,
    Column,
    Container,
    FontWeight,
    Image,
    MainAxisAlignment,
    Row,
    Text,
    margin,
    padding,
)
import flet as ft

card_cultura = Card(
    content=Container(
        bgcolor="white",
        height=95,
        width=300,
        border_radius=11,
        padding=padding.only(left=20),
        content=Row(
            controls=[
                Container(
                    Image(
                        src=f"assets/icons/corn.png",
                        width=300,
                        height=300,
                    ),
                    margin=margin.only(left=-60, right=-180),
                ),
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Container(
                            Text(
                                "Milho",
                                color="#000000",
                                size=17,
                                weight=FontWeight.W_600,
                            ),
                            margin=margin.only(bottom=-14),
                        ),
                        Text(
                            "Plantio: 255/08/2022 \nÁrea: 5000m² \nEstágio: Maturação",
                            color="#000000",
                            size=10,
                            weight=FontWeight.W_600,
                        ),
                    ],
                ),
            ],
        ),
    ),
    elevation=4,
)

card_irrigacao = Container(
    Container(
        bgcolor="white",
        height=140,
        width=140,
        border_radius=11,
        padding=padding.only(top=14, left=17, right=17, bottom=22),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            bgcolor="#EBEBF0",
                            height=24,
                            width=75,
                            border_radius=20,
                            margin=margin.only(right=7),
                            content=ft.Text(
                                "Irrigação",
                                color="#000000",
                                size=12,
                                weight=FontWeight.W_700,
                            ),
                        ),
                        Image(
                            src=f"/icons/watch.svg",
                            width=20,
                            height=20,
                        ),
                    ]
                ),
                Container(
                    Text(
                        value="1h30", color="#000000", size=39, weight=FontWeight.W_700
                    ),
                    margin=margin.only(top=-10),
                ),
                Container(
                    Text(
                        value="Tempo ideal de irrigação para hoje",
                        color="#000000",
                        size=11,
                        weight=FontWeight.W_400,
                    )
                ),
            ]
        ),
    ),
)

card_economia = Container(
    Container(
        bgcolor="white",
        height=140,
        width=140,
        border_radius=11,
        padding=padding.only(top=14, left=17, right=17, bottom=22),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            bgcolor="#EBEBF0",
                            height=24,
                            width=75,
                            border_radius=20,
                            margin=margin.only(right=7),
                            content=ft.Text(
                                "Economia",
                                color="#000000",
                                size=12,
                                weight=FontWeight.W_700,
                            ),
                        ),
                        Image(
                            src=f"/icons/percentage.svg",
                            width=20,
                            height=20,
                        ),
                    ]
                ),
                Container(
                    Text(
                        value="27%", color="#000000", size=39, weight=FontWeight.W_700
                    ),
                    margin=margin.only(top=-10),
                ),
                Container(
                    Text(
                        value="760 litros",
                        color="#000000",
                        size=11,
                        weight=FontWeight.W_400,
                    ),
                    Text(
                        value="economizados",
                        color="#000000",
                        size=11,
                        weight=FontWeight.W_400,
                    ),
                ),
            ]
        ),
    ),
)
