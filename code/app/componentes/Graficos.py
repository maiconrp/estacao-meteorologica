import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from flet.plotly_chart import PlotlyChart
from flet import UserControl
import assets.colors
from database import valores_etc, dict_temp, grafico_temp, grafico_etc



class GraficoBarras(UserControl):
    def build(self):
        green = [assets.colors.PRIMARY_GREEN,]*100
        cinza_claro = [assets.colors.CINZA_AZULADO,]*100
        fig = go.Figure()

        dias = [v.key() for v in valores_etc.each()]
        fig.add_trace(go.Bar(x=dias,
                        y=[v.val() for v in valores_etc.each()],
                        marker_color=green
                        ))

        #fig = px.bar(df, x='index', y='value', color=green)

        fig.update_layout(
            title='Evapotranspiração',
            titlefont_size=28,
            yaxis=dict(
                title='mm/dia',
                titlefont_size=22,
                tickfont_size=14,
            ),
            xaxis=dict(
                title='Dia',
                titlefont_size=22,
                tickfont_size=18,
            ),
            legend=dict(
                x=1.0,
                y=1.0,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.1, # gap between bars of adjacent location coordinates.
            bargroupgap=0.1 # gap between bars of the same location coordinate.
        )
        
        return PlotlyChart(fig, expand=True)

grafico_Etc = GraficoBarras()

class GraficoLinhas(UserControl):
    def build(self):
        green = [assets.colors.PRIMARY_GREEN,]*100
        cinza_claro = [assets.colors.CINZA_AZULADO,]*100
        
        fig = go.Figure()

        dias = [v.key() for v in dict_temp.each()]

        print(dias)

        fig.add_trace(go.Scatter(x=dias, 
            y=[v.val() for v in dict_temp.each()], 
            line=dict(color='#00D154', 
            width=6)))

        fig.update_layout(
            title='Temperatura',
            titlefont_size=28,
            yaxis=dict(
                title='Valor em °C',
                titlefont_size=22,
                tickfont_size=14,
            ),
            xaxis=dict(
                title='Dia',
                titlefont_size=22,
                tickfont_size=18,
            ),
            legend=dict(
                x=1.0,
                y=1.0,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.1, # gap between bars of adjacent location coordinates.
            bargroupgap=0.1 # gap between bars of the same location coordinate.
        )
        return PlotlyChart(fig, expand=True)

grafico_temperatura = GraficoLinhas()