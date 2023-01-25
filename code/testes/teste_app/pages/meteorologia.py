from componentes.TextField import pressao, radiacao, temperatura, umidade, vento
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
import flet as ft

class MeteorologiaPage:
    def build():
        return ft.View(
                "/Meteorologia",
                [
                    appbar,
                    ft.Column(
                    [
                        pressao,
                        radiacao,
                        temperatura,
                        umidade,
                        vento
                    ]
                    ),
                    navigation_bar,
                ],
                vertical_alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

            )
