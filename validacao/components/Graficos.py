import plotly.express as px
import plotly.graph_objects as go
import os
from flet.plotly_chart import PlotlyChart
from flet import* 
from Utils.historicos import *

class GraficoLinhas(UserControl):
    def __init__(
        self,
        dicio_INMET = None,
        dicio_EST = None,
        title_graph = None,
        titley = None,
        medicoes=None,

    ):
        super().__init__()
        self.dicio_INMET = dicio_INMET
        self.dicio_EST = dicio_EST
        self.title_graph = title_graph
        self.titley = titley
        self.medicoes = medicoes

    def build(self):
        fig = go.Figure()

###         CRIANDO O GRÁFICO COM 2 LINHAS, CADA UMA REPRESENTANDO O HISTÓRICO DE UMA ESTAÇÃO      ###

        fig.add_trace(go.Scatter(x=[v for v in self.dicio_INMET.keys()], 
            y=self.medicoes,
            name='INMET',
            mode='lines+markers',
            marker=dict(
                size=2, 
                color='#525A64',
                line=dict(
                    color='#525A64', 
                    width=1)
            ), 
            textfont=dict(size=1),
            ))
        
        fig.add_trace(go.Scatter(x=[v for v in self.dicio_EST.keys()], 
            y=[v for v in self.dicio_EST.values()],
            name='Nossa estação',
            mode='lines+markers',
            marker=dict(
                size=2, 
                color='#00D154',
                line=dict(
                    color='#00D154', 
                    width=1
                ),
            ),
            textfont=dict(size=1),
            ),
        )
     
        fig.update_layout(
            width=320,  
            height=130,
            title=self.title_graph,
            titlefont_size=8,
            margin=dict(t=20, b=20),
            font=dict(
                size=5,  # Defina o tamanho da fonte desejado
            ),
            yaxis=dict(
                title=self.titley,
                titlefont_size=3,
                tickfont_size=3,
                title_standoff=10, 
                #range=[15, 30],
            ),
            xaxis=dict(
                title='Hora (UTC)',
                titlefont_size=3,
                tickfont_size=3,
                title_standoff=5, 
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

        return PlotlyChart(fig, expand=False)


if path_json == '' or path_csv == '':
    content = Text('Informe o caminho do diretório da tabela')
else:
    ### Cria os gráficos

    #GraficoRadINMET = GraficoLinhas(path_csv=path_csv, parametro = "Radiacao (KJ/m)", title_graph = 'Radiação', titley='Valor em KJ')
    GraficoTemp = GraficoLinhas(dicio_EST = historico_temperatura_EST, dicio_INMET = historico_temperatura_INMET, 
                                medicoes =  medicoes_temperatura, title_graph = 'Temperatura', titley='Valor em °C')

    GraficoUmi = GraficoLinhas(dicio_EST = historico_umidade_EST, dicio_INMET = historico_umidade_INMET, 
                                medicoes =  medicoes_umidade, title_graph = 'Umidade', titley='Valor em %')

    #GraficoVentoINMET = GraficoLinhas(path_csv=path_csv, parametro = "Vel. Vento (m/s)", title_graph = 'Vento', titley='Valor em m/s') 
    #GraficoTempEST = GraficoLinhas(path=path_json, parametro = "temperatura", title_graph = 'Temperatura da estação', titley='Valor em °C')
    #GraficoUmiEST= GraficoLinhas(path=path_json, parametro = "umidade", title_graph = 'Umidade', titley='Valor em %') 
    #GraficoRadEST = GraficoLinhas(path=path, parametro = radiacao, title_graph = 'radiacao', titley='Valor em KJ/m²') 
    #GraficoVentoEST = GraficoLinhas(path=path, parametro = vento, title_graph = 'vento', titley='Valor em m/s') 









