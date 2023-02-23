import flet as ft

# Import dos componentes da aplicação
from componentes.AppBar import appbar
from componentes.NavigationBar import navigation_bar
from componentes.botões.ElevatedButton import ElevatedButton
from componentes.TextField import pressao, radiacao, temperatura, umidade, vento
from config.firebase import database

# Import da classe de rotas
from routes import Route

def main(page: ft.Page):
    # Função para configurar o título, alinhamento horizontal e modo de tema da página
    def config():
        page.title = "Estacao Meteorologica"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = "dark"
        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

    # Função para definir os eventos dos componentes
    def set_events():

        # Evento de clique na ação de menu de appbar
        

        # Evento de clique no botão ElevatedButton
        ElevatedButton.on_click=lambda _: page.go("/login")

        # Evento de mudança de seleção na barra de navegação
        navigation_bar.on_change = navigation_bar_change

        # Eventos de mudança nos campos de texto
        pressao.on_change       =   lambda _: page.update() 
        radiacao.on_change      =   lambda _: page.update() 
        temperatura.on_change   =   lambda _: page.update() 
        umidade.on_change       =   lambda _: page.update() 
        vento.on_change         =   lambda _: page.update() 

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
        rotas = Route.get_routes()

        # Ir para a rota selecionada
        page.go(rotas[index])
        
    # Função para tratar a mudança de rota
    def route_change(route):
        # Limpar a lista de vistas
        page.views.clear()
        # Adicionar a vista destino à lista
        page.views.append(Route.get_destiny(page.route))
        # Atualizar a página
        page.update()

    # Função que remove a última vista da lista
    def view_pop(view):
        # Remover a última vista da lista
        page.views.pop()
        # Obter a vista no topo da lista
        top_view = page.views[-1]
        # Ir para a rota da vista no topo da lista
        page.go(top_view.route)

    config()
    set_events()

ft.app(target=main)