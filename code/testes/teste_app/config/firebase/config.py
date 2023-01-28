import pyrebase # biblioteca pra comunicação com firebase
import json # biblioteca pra ler o arquivo json de configurações firebase
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# credenciais de comunicação
with open(BASE_DIR+"\config.json", 'r') as f:
    CONFIG = json.load(f)

# configura comunicação com firebase
FIREBASE = pyrebase.initialize_app(CONFIG)