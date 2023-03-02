import flet as ft
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton
from componentes.Container import container_home

# page
# page.go
class HomePage:
    
    def build():
        return ft.View(
                "/",
                [
                    container_home
                ],
            )
