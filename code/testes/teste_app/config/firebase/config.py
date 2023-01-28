import pyrebase # biblioteca para comunicação com firebase
import json # biblioteca para ler o arquivo JSON de configurações do Firebase
import os

# Diretório base da aplicação
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Carrega as credenciais de comunicação com o Firebase
with open(os.path.join(BASE_DIR, "config.json"), 'r') as f:
    CONFIG = json.load(f)

# Configura a comunicação com o Firebase
FIREBASE = pyrebase.initialize_app(CONFIG)
