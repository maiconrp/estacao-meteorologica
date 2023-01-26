import pyrebase # biblioteca pra comunicação com firebase
import json # biblioteca pra ler o arquivo json de configurações firebase

# credenciais de comunicação
with open(r"teste_app\config\firebase\config.json", 'r') as f:
    CONFIG = json.load(f)

# configura comunicação com firebase
FIREBASE = pyrebase.initialize_app(CONFIG)