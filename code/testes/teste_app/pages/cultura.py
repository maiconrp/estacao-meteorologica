import flet as ft
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton
from componentes.Container import container_home, container_cultura

# page
# page.go
class CulturaPage:
    
    def build():
        return ft.View(
                "/cultura",
                [              
                    container_cultura,  
                ],
            )