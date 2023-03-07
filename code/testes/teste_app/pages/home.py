import flet as ft
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton
from componentes.Container import *
from componentes.Container import card_cultura

# page
# page.go
class HomePage:
    def build():
        return ft.View(
            "/",
            [
            Column(
                controls=[
                    card_cultura,
                    line,
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
