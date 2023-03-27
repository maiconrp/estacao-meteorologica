import flet as ft
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton
from componentes.Container import *
from componentes.Graficos import grafico_temperatura, grafico_Etc



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
                        grafico_Etc,
                    ],
                    horizontal_alignment="center",
                ),
                navigation_bar,
            ],
            scroll="auto",
            appbar=appbar,
            horizontal_alignment="center",
        )
