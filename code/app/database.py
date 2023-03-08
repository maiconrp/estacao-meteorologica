"""
Descrição:  
    Este código é responsável por estabelecer uma conexão com o banco de dados do Firebase e 
    monitorar os dados meteorológicos armazenados nele.

Importações:
    - 'config.FIREBASE': Importa a configuração do Firebase.
    - 'componentes.TextField': Importa cinco componentes de texto (pressão, radiação, temperatura, umidade e vento)

Variáveis:
    - 'db': Instância do banco de dados Firebase inicializado a partir da configuração importada.
    - 'path': String que define o caminho padrão para acesso às informações meteorológicas no Firebase.
    - 'componentes': Dicionário que associa cada tipo de dado meteorológico ao seu respectivo componente de texto.
    - 'variaveis_firebase': Lista das variáveis meteorológicas monitoradas.
    - 'streams': Dicionário para armazenar referências aos streams criados para monitorar as variáveis meteorológicas.

Funções:
    - 'stream': Função que atualiza os valores dos componentes de texto quando houver mudanças no Firebase. 
                Recebe um dicionário 'message' e busca o componente correspondente ao tipo de dado meteorológico recebido. 
                Em seguida, atualiza o valor do componente com o dado recebido.

Classes:
    - Nenhuma classe é declarada neste código.

Loops:
    - "for" : Inicializa todas as conexões com as variáveis monitoradas no Firebase. 
              Para cada uma dessas variáveis, é criado um stream que monitora as atualizações nesse dado. 
              O stream é adicionado ao dicionário 'streams' para ser mantido como uma referência.

"""

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
variaveis_firebase = [
    "pressao", 
    "radiacao", 
    "temperatura", 
    "umidade", 
    "vento"
]

streams: dict = {}

# Função para atualizar os valores dos componentes de texto quando houver mudanças no Firebase
def stream(message):
    # Busca o componente correspondente ao tipo de dado meteorológico recebido
    componente = componentes.get(message["stream_id"])
    # Atualiza o valor do componente
    componente.value = message["data"]
    
# Inicialização dos streams de dados do Firebase para cada tipo de dado meteorológico
for variavel in variaveis_firebase:
    streams[variavel] = db.child(path.format(variavel)).stream(stream, stream_id=variavel)

print(streams)

# pressao_stream = db.child(path.format("pressao")).stream(stream, stream_id="pressao")
# radiacao_stream = db.child(path.format("radiacao")).stream(stream, stream_id="radiacao")
# temperatura_stream = db.child(path.format("temperatura")).stream(stream, stream_id="temperatura")
# umidade_stream = db.child(path.format("umidade")).stream(stream, stream_id="umidade")
# vento_stream = db.child(path.format("vento")).stream(stream, stream_id="vento")

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
"""
