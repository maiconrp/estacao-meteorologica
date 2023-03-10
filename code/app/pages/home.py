import flet as ft
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton
from componentes.Container import *


class HomePage:
    def build():
        return ft.View(
            "/",
            [
                Column(
                    controls=[
                        card_cultura,
                        line,
                        clima,
                        Card(temperatura, elevation=8),
                        Card(umidade, elevation=8),
                        Card(vento, elevation=8),
                        Card(pressao, elevation=8),
                        Card(radiacao, elevation=4),
                        relatorio,
                        Row(
                            controls=[
                                Card(card_irrigacao, elevation=6),
                                Card(card_economia, elevation=6),
                            ],
                            alignment="center",
                        ),
                        Card(card_ET, elevation=6),
                    ],
                    horizontal_alignment="center",
                ),
                navigation_bar,
            ],
            appbar=appbar,
            horizontal_alignment="center",
        )
