###     ESTE ARQUIVO CRIA OS DICIONÁRIOS QUE REPRESENTAM 
###     OS HISTÓRICOS DOS VALORES COLETADOS DE UM DIA ESPECÍFICO   

import numpy as np
import pandas as pd


### Caminhos do diretório de cada tipo de arquivo
### Por enquanto, para cada tabela de um dia, de cada estação, é necessário alterar o caminho manualmente aqui no código.
path_json='C:\\Users\\Victor Fonteles\\Documents\\validacao\\Tables\\Estacao\\01-06-2023.json'
path_csv='C:\\Users\\Victor Fonteles\\Documents\\validacao\\Tables\\INMET\\05-06-2023-INMET.csv'

# A partir do csv baixado, essa função irá criar um dicionário que relaciona os horários com 
# os valores coletados de um parâmetro climático 
def GerarHistóricoInmet(path, parametro):
    ###     Criando dataframe do arquivo csv, que foi baixado diretamento do site do INMET: https://mapas.inmet.gov.br/, a partir da estação desejada
    df = pd.read_csv(path_csv, encoding='ISO-8859-1')

    #transforma o dataframe 'df' em um dicionario python
    dicionario_clima = df.to_dict()

    #Cria o dict 'horas', onde cada chave recebe o um valor da chave 'Hora (UTC)' do 'dicionario_clima'
    horas =  dicionario_clima['Hora (UTC)']

    # Atualiza os valores deixando o horário no formato HH:MIN
    horas = {key: f"{str(value).zfill(4)[:2]}:{str(value).zfill(4)[2:]}" for key, value in horas.items()}

    #Cria o dict 'valores', onde cada chave recebe um valor das chaves do parametro climatologico do 'dicionario_clima'
    valores = dicionario_clima[parametro]

    #Cria o dicionário que irá de fato contes o históricco dos valores
    dict_historico_INMET = {}

    ###     Preenche o dicionário relacionando as horas com os respectivos valores      ###
    i=0
    for hora in horas.values():
        valor = valores[i]
        dict_historico_INMET[hora] = valor
        i=i+1


    return dict_historico_INMET

# A partir do json baixado, essa função irá criar um dicionário que relaciona os horários com 
# os valores coletados de um parâmetro climático    
def GerarHistóricoEst(path, parametro):
    ###     Cria o dataframe do arquivo json, que foi exortado do firebase
    df = pd.read_json(path, encoding='ISO-8859-1')

    ### Cria um dicionário que contém somente a coluna do parâmetro desejado
    ### Este dicionário já relaciona os valores coletados com sua respectiva hora
    dict_historico_EST = df["Produtor"]["Cultura"]["Meteorologia"][parametro]

   
    return dict_historico_EST

# Cria a lista "medicoes", que irá guardar os valores medidos daquele parâmetro climático, 
# convertidos em float
def GerarListaMedicoes(dicio, parametro):
    if parametro == 'Temp. Ins. (C)' or parametro== 'Vel. Vento (m/s)' or parametro =='Radiacao (KJ/m)':
        ###     Percorre cada valor, e substitui a virgula por ponto, transformando em tipo float.
        try:
            medicoes = [float(v.replace(',', '.')) for v in dicio.values() if type(v) != 'NoneType']
        except:
            medicoes = [i for i in range(24)]
    else:
        ###     Se o parâmetro for 'umidade', apenas percorre   os valores, transformando eles em int.         
        try:
            medicoes = [int(v) for v in dicio.values() if type(v) != 'NoneType']
        except:
            medicoes = [i for i in range(24)]

    return medicoes


historico_temperatura_INMET = GerarHistóricoInmet(path_csv, "Temp. Ins. (C)")
historico_umidade_INMET = GerarHistóricoInmet(path_csv, "Umi. Ins. (%)")


medicoes_temperatura = GerarListaMedicoes(historico_temperatura_INMET, 'Temp. Ins. (C)')
medicoes_umidade = GerarListaMedicoes(historico_umidade_INMET, 'Umi. Ins. (%)')

historico_temperatura_EST = GerarHistóricoEst(path_json, "temperatura")
historico_umidade_EST = GerarHistóricoEst(path_json, "umidade")


