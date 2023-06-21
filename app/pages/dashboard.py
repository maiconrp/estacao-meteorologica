import flet as ft
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton
from componentes.Container import *
from componentes.Card import card_cultura
from componentes.Graficos import grafico_temperatura



class DashBoardPage:
    def build():
        return ft.View(
            "/dashboard",
            [
                Column(
                    controls=[
                        card_cultura,
                        line,
                        grafico_temperatura,
                    ],
                    horizontal_alignment="center",
                ),
                navigation_bar,
            ],
            scroll="auto",
            appbar=appbar,
            horizontal_alignment="center",
        )
