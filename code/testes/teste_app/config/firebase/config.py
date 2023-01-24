# pip install pyrebase
import pyrebase # biblioteca pra comunicação com firebase

# Credenciais de comunicação, disponíveis em: 
# https://console.firebase.google.com/u/0/project/estacao-meteorologic/settings/general/web:MTZhYzBhNjMtY2JiNy00ZmM5LTlhYzgtMmEwOWM1MzJkOWZi?hl=pt
CONFIG = {
    "apiKey": "apiKey",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "projectId.appspot.com"
}

# configura comunicação com firebase
FIREBASE = pyrebase.initialize_app(CONFIG)