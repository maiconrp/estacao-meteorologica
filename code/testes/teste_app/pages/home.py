import flet as ft
import routes
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton

# page
# page.go
class HomePage:
    def build():
        return ft.View(
                "/",
                [
                    appbar,
                    HomeButton,
                    navigation_bar
                ],
            )
