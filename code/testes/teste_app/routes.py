from pages.home import HomePage
from pages.login import LoginPage
from pages.cultura import CulturaPage
    
class Route:
    # Define as rotas disponíveis no aplicativo, com o caminho da rota como chave e o destino (página ou componente) como valor
    ROUTES = {
        "/cultura": CulturaPage.build(), # Rota para a página de meteorologia
        "/": HomePage.build(), # Rota para a página inicial     
    }

    @classmethod
    def get_destiny(cls, route):
        # Retorna o destino (página ou componente) associado à rota especificada
        return cls.ROUTES.get(route, "/")

    @classmethod
    def get_routes(cls):
        # Retorna uma lista de todas as rotas disponíveis no aplicativo
        return list(cls.ROUTES.keys())

