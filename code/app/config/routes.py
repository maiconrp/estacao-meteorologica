from pages.home import HomePage
from pages.meteorologia import MeteorologiaPage
from pages.auth.login import LoginPage
from flet import UserControl
import flet as ft


class RouteConfig(UserControl):
    """
    Classe que representa as rotas disponíveis no aplicativo web.
    """

    # Define as rotas disponíveis no aplicativo, com o caminho da rota como chave e o
    # destino (página ou componente) como valor
    ROUTES = {
        "/meteorologia": MeteorologiaPage.build(),
        "/": HomePage.build(),
        "/login": LoginPage.build(),
    }

    def did_mount(self):
        """
        Método que é chamado após a criação do objeto.
        Configura os eventos de mudança de rota e de remoção da última vista.
        """
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(self.page.route)

    def route_change(self, route):
        """
        Método que trata a mudança de rota.
        Limpa a lista de vistas e adiciona a vista destino à lista.
        """
        self.page.views.clear()
        self.page.views.append(self.get_destiny(self.page.route))
        self.page.update()

    def view_pop(self, view):
        """
        Método que remove a última vista da lista.
        """
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def get_destiny(self, route):
        """
        Método que retorna o destino (página ou componente) associado à rota especificada.
        Se a rota não estiver presente em ROUTES, retorna a página inicial.
        """
        # Retorna o destino (página ou componente) associado à rota especificada
        return self.ROUTES.get(route, "/")

    def get_routes(self):
        """
        Método que retorna uma lista de todas as rotas disponíveis no aplicativo.
        """
        # Retorna uma lista de todas as rotas disponíveis no aplicativo
        return list(self.ROUTES.keys())

    def go_route(self, index):
        """
        Método que vai para a rota correspondente ao índice especificado.
        """
        self.page.go(self.get_routes()[index])

    def build(self):
        """
        Método que cria o objeto.
        """
        return ft.Container()
