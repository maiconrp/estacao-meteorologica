import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from flet.plotly_chart import PlotlyChart
from flet import UserControl
import assets.colors
from database import variaveis

class GraficoBarras(UserControl):
    def build(self):
        green = [assets.colors.PRIMARY_GREEN,]*100
        cinza_claro = [assets.colors.CINZA_AZULADO,]*100

        years = [v.val() for v in variaveis.each()]
        print(years)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=years,
                        y=[v.val() for v in variaveis.each()],
                        name='Rest of world',
                        marker_color=green
                        ))

        fig.update_layout(
            title='Temperatura',
            xaxis_tickfont_size=14,
            yaxis=dict(
                title='Valor (°C)',
                titlefont_size=14,
                tickfont_size=14,
            ),
            xaxis=dict(
                title='Hora',
                titlefont_size=14,
                tickfont_size=14,
            ),
            legend=dict(
                x=0,
                y=1.0,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.15, # gap between bars of adjacent location coordinates.
            bargroupgap=0.1 # gap between bars of the same location coordinate.
        )
        
        return PlotlyChart(fig, expand=True)

grafico_barras = GraficoBarras()

class GraficoLinhas(UserControl):
    def build(self):
        df = px.data.gapminder().query("country=='Canada'")
        df = pd.DataFrame(dict(
            variaveis.each()
        ))
        fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

        return PlotlyChart(fig, expand=True)

grafico_linha = GraficoLinhas()