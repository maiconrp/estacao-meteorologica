from config.py import FIREBASE
from componentes.TextField import pressao, radiacao, temperatura, umidade, vento

db = FIREBASE.database()

Produtor = db.child("Produtor")
Cultura = Produtor.child("Cultura")
Meteorologia = Cultura.child("Meteorologia")

class MeteorologiaStream:
    def __init__(self, variavel, objeto):
        self.variavel = db.child(variavel)
        self.variavel_stream = self.variavel.stream(self.stream_variavel)
        self.objeto = objeto

    def stream_variavel(self, message):
        objeto.value = message["data"]
        page.update()
        
    def start(self):
        self.vento_stream.start()

class FirebaseValor:
    def __init__(self, nome, caminho, campo):
        self.nome = nome
        self.caminho = caminho
        self.campo = campo

    def start():
        caminhos_valores + nome + "valor_atual"
        pass

def stream_pressão(message):
    pressao.value = message["data"] # altera o valor do elemento (pressao.value) e atualiza
    page.update()

def stream_radiacao(message):
    radiacao.value = message["data"]
    page.update()

def stream_temp(message):
    temperatura.value = message["data"]
    page.update()

def stream_umidade(message):
    umidade.value = message["data"]
    page.update()

def stream_vento(message):
    vento.value = message["data"]
    page.update()
    
# Pega cada valor de info clima e manda pra função monitorar ^
firebase_pressao = Meteorologia.child("pressao/valor_atual").stream(stream_pressao)
radiacao_stream = Meteorologia.child("radiacao/valor_atual").stream(stream_vento)
temperatura_stream = Meteorologia.child("temperatura/valor_atual").stream(stream_temp)
umidade_stream = Meteorologia.child("umidade/valor_atual").stream(stream_umidade)
vento_stream = Meteorologia.child("vento/valor_atual").stream(stream_vento)


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
