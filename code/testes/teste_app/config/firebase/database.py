"""
Este código é responsável por estabelecer uma conexão com o banco de dados do Firebase, 
e monitorar as variações dos valores de pressão, radiação, temperatura, umidade e vento. 
Quando houver uma atualização nos valores dessas variáveis, a função "stream" é chamada 
e atualiza o valor exibido no campo de texto correspondente.

Importações:
- O módulo 'config' é importado para obter a configuração do Firebase.
- Os componentes 'TextField' são importados para exibir os valores das variáveis monitoradas.

Variáveis:
- 'db': objeto que representa a conexão com o banco de dados do Firebase.
- 'path': string com o caminho para as variáveis monitoradas no banco de dados.
- 'pressao', 'radiacao', 'temperatura', 'umidade' e 'vento': objetos do tipo 'TextField' que exibem os valores das variáveis monitoradas.
- 'pressao_stream', 'radiacao_stream', 'temperatura_stream', 'umidade_stream' e 'vento_stream': objetos que representam a conexão com as variáveis monitoradas no banco de dados.

Funções:
- 'stream': é chamada sempre que há uma atualização nos valores das variáveis monitoradas. 
            Ela recebe como parâmetro a mensagem com o novo valor e atualiza o valor exibido 
            no campo de texto correspondente.
"""

from .config import FIREBASE
from componentes.TextField import pressao, radiacao, temperatura, umidade, vento

# Inicialização do banco de dados do Firebase
db = FIREBASE.database()

# Caminho padrão para acesso às informações meteorológicas
path = "/Produtor/Cultura/Meteorologia/{}/valor_atual"

# Dicionário para associar cada tipo de dado meteorológico ao seu respectivo componente de texto
componentes = {
    "pressao": pressao,
    "radiacao": radiacao,
    "temperatura": temperatura,
    "umidade": umidade,
    "vento": vento,
}

# Função para atualizar os valores dos componentes de texto quando houver mudanças no Firebase
def stream(message):
    # Busca o componente correspondente ao tipo de dado meteorológico recebido
    componente = componentes.get(message["stream_id"])
    # Atualiza o valor do componente
    componente.value = message["data"]
    
# Inicialização dos streams de dados do Firebase para cada tipo de dado meteorológico
pressao_stream = db.child(path.format("pressao")).stream(stream, stream_id="pressao")
radiacao_stream = db.child(path.format("radiacao")).stream(stream, stream_id="radiacao")
temperatura_stream = db.child(path.format("temperatura")).stream(stream, stream_id="temperatura")
umidade_stream = db.child(path.format("umidade")).stream(stream, stream_id="umidade")
vento_stream = db.child(path.format("vento")).stream(stream, stream_id="vento")

# class MeteorologiaStream:
#     def __init__(self, variavel, objeto):
#         self.variavel = db.child(variavel)
#         self.variavel_stream = self.variavel.stream(self.stream_variavel)
#         self.objeto = objeto

#     def stream_variavel(self, message):
#         objeto.value = message["data"]
#         page.update()
        
#     def start(self):
#         self.vento_stream.start()

# class FirebaseValor:
#     def __init__(self, nome, caminho, campo):
#         self.nome = nome
#         self.caminho = caminho
#         self.campo = campo

#     def start():
#         caminhos_valores + nome + "valor_atual"
#         pass

# pegar banco de dados

# def stream_database():

#     db = DATABASE
#  # Altera o valor sempre que ele atualiza no banco
#     def stream_pressão(message):
#         pressao.value = message["data"] # altera o valor do elemento (pressao.value) e atualiza
#         page.update()

#     def stream_radiacao(message):
#         radiacao.value = message["data"]
#         page.update()
    
#     def stream_temp(message):
#         temperatura.value = message["data"]
#         page.update()

#     def stream_umidade(message):
#         umidade.value = message["data"]
#         page.update()

#     def stream_vento(message):
#         vento.value = message["data"]
#         page.update()

    
#     # Pega cada valor de info clima e manda pra função monitorar ^
#     pressao_stream = db.child("InfoClima").child(
#         "Pressão").child("ultimo valor").stream(stream_pressão)
#     radiacao_stream = db.child("InfoClima").child(
#         "Radiacao").child("ultimo valor").stream(stream_radiacao)
#     temperatura_stream = db.child("InfoClima").child(
#         "Temperatura").child("ultimo valor").stream(stream_temp)
#     umidade_stream = db.child("InfoClima").child(
#         "Umidade").child("ultimo valor").stream(stream_umidade)
#     vento_stream = db.child("InfoClima").child(
#         "Vento").child("ultimo valor").stream(stream_vento)

# class Database:
#     def init(self, value, access_method):
#         self.value = value
#         self.access_method = access_method
#         self.db = FIREBASE.database()

#     def stream_database(self):
#         if self.access_method == "stream":
#             def stream_value(message):
#                 self.value.value = message["data"]
#                 page.update()

#             value_stream = self.db.child("InfoClima").child(
#                 self.value).child("ultimo valor").stream(stream_value)
#         elif self.access_method == "get":
#             value = self.db.child("InfoClima").child(
#                 self.value).child("ultimo valor").get()
#             self.value.value = value
#             page.update()
#         else:
#             print("Método de acesso inválido.")

#     pressao = Database("Pressão", "stream")
#     pressao.stream_database()
#     radiacao = Database("Radiacao", "stream")
#     radiacao.stream_database()
#     temperatura = Database("Temperatura", "stream")
#     temperatura.stream_database()
#     umidade = Database("Umidade", "stream")
#     umidade.stream_database()
#     vento = Database("Vento", "stream")
#     vento.stream_database()
