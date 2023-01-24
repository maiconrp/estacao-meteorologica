import flet as ft
import routes
from componentes.botões.ElevatedButton import LoginButton
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar

class LoginPage:
    def build():
        return ft.View(
                "/login",
                [
                    appbar,
                    LoginButton,
                    navigation_bar
                ],
            )
