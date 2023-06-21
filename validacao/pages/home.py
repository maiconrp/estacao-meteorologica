import flet as ft
from flet import*
from components.Graficos import GraficoUmi, GraficoTemp
from components.Container import data, dados_temp, dados_umi


class HomePage:
    def build():
        return ft.View(
            "/",
            [
                Column(
                    controls = [
                        data,
                        GraficoTemp,
                        dados_temp,
                        GraficoUmi,
                        dados_umi,
                     ]   
                )
            ],
            scroll="auto",
            horizontal_alignment="center",
        )
