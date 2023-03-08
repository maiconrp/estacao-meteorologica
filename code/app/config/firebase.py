"""
import pyrebase 
import json 
import os

class FirebaseConfig(UserControl):
    def __init__(self):
        super().__init__()
        # Diretório base da aplicação
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        # Carrega as credenciais de comunicação com o Firebase
        with open(os.path.join(self.BASE_DIR, "config.json"), 'r') as f:
            self.CONFIG = json.load(f)
            
        # Configura a comunicação com o Firebase
        self.FIREBASE = pyrebase.initialize_app(self.CONFIG)
    
    def build(self):
        \"""
        Método que cria o objeto.
        \"""
        return ft.Container()

"""
