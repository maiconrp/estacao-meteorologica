import flet as ft
from componentes.Container import Irrigacao, Evapotranspiracao, Economia
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
                    Irrigacao, 
                    Economia,
                    Evapotranspiracao, 
                    navigation_bar
                ],
            )

