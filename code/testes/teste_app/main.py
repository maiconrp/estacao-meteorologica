import flet as ft

from componentes.AppBar import appbar
from componentes.NavigationBar import navigation_bar
from componentes.botões.ElevatedButton import ElevatedButton
from componentes.TextField import pressao, radiacao, temperatura, umidade, vento
from config.firebase import database

from routes import Route

def main(page: ft.Page):
    def config():
        page.title = "Estacao Meteorologica"
        vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = "dark"
        textColor = ft.colors.WHITE
        bgCor = ft.colors.GREEN_900

    def set_events():
        appbar.actions[2].items[2].on_click=check_item_clicked
        ElevatedButton.on_click=lambda _: page.go("/login")

        navigation_bar.on_change = navigation_bar_change

        pressao.on_change=lambda _: page.update() 
        radiacao.on_change=lambda _: page.update() 
        temperatura.on_change=lambda _: page.update() 
        umidade.on_change=lambda _: page.update() 
        vento.on_change=lambda _: page.update() 

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def navigation_bar_change(e):
        index = e.control.selected_index
        print("e control:", e.control.selected_index)
        rotas = Route.get_routes()
        page.go(rotas[index])
        
    def route_change(route):
        page.views.clear()
        page.views.append(Route.get_destiny(page.route))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    config()
    set_events()
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)