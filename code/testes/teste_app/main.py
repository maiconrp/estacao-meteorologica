import flet as ft

import assets.colors
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import ElevatedButton
from componentes.NavigationBar import navigation_bar
from componentes.TextField import pressao, radiacao, temperatura, umidade, vento
from config import settings
from config.firebase import database
from routes import Route


def main(page: ft.Page):
    page.add(settings.PageConfig())
    rotas = Route()

    page.add(rotas)

    # Função para definir os eventos dos componentes
    def set_events():

        # Evento de clique na ação de menu de appbar

        # Evento de clique no botão ElevatedButton
        ElevatedButton.on_click = lambda _: page.go("/login")

        # Evento de mudança de seleção na barra de navegação
        navigation_bar.on_change = navigation_bar_change

        # Eventos de mudança nos campos de texto
        pressao.on_change = lambda _: page.update()
        radiacao.on_change = lambda _: page.update()
        temperatura.on_change = lambda _: page.update()
        umidade.on_change = lambda _: page.update()
        vento.on_change = lambda _: page.update()

    # Função para verificar se o item de menu foi clicado
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    # Função para tratar a mudança de seleção na barra de navegação
    def navigation_bar_change(e):

        # Índice selecionado na barra de navegação
        index = e.control.selected_index
        print("e control:", e.control.selected_index)

        # Lista de rotas
        # Ir para a rota selecionada
        rotas.go_route(index)

    set_events()


ft.app(target=main, assets_dir="assets")
