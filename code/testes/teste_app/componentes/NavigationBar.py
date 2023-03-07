from flet import NavigationBar, NavigationDestination, icons

import flet as ft
from flet import *

destinations = [
    ft.NavigationDestination(
        icon_content=Image(
            src=f"assets/icons/navbar/plant.svg",
            width=16,
        ),
        label="Cultura",
    ),
    ft.NavigationDestination(
        icon_content=Image(
            src=f"assets/icons/navbar/home.svg",
            width=20,
        ),
        label="Home",
    ),
    ft.NavigationDestination(
        icon_content=Image(
            src=f"assets/icons/navbar/user.svg",
            width=16,
        ),
        label="Perfil",
    ),
]


class NavigationBarTemplate(NavigationBar):
    """
    Classe para criar uma barra de navegação com configurações comuns

    Atributos:
        ATRIBUTO       TIPO                            DEFINIÇÃO
        destinations   (List[NavigationDestination])   lista de destinos de navegação
    """

    def __init__(
        self,
        destinations=destinations,
        bgcolor="#FFFFFF",
        width=390,
        height=70,
        border_radius=border_radius.only(bottomLeft=15, bottomRight=15),
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.destinations = destinations
        self.bgcolor = bgcolor
        self.width = width
        self.height = height
        self.border_radius = border_radius


navigation_bar = NavigationBarTemplate()
