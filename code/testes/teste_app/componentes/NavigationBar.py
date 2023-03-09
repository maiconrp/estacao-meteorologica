from flet import (
    NavigationBar,
    NavigationBarLabelBehavior,
    NavigationDestination,
    Image,
    UserControl,
    border_radius,
    Container,
)
import config.routes

import flet as ft
class NavigationDestinationTemplate(NavigationDestination):
    def __init__(self, icon, label="Cultura", width=16):
        super().__init__()
        self.label = label
        self.icon_content = Image(src=f"assets/icons/navbar/{icon}.svg", width=width)


# class NavigationBarTemplate(NavigationBar):
#     """
#     Classe para criar uma barra de navegação com configurações comuns

#     Atributos:
#         ATRIBUTO       TIPO                            DEFINIÇÃO
#         destinations   (List[NavigationDestination])   lista de destinos de navegação
#     """

#     def __init__(
#         self,
#         destinations=[
#             NavigationDestinationTemplate(label="Cultura", icon="plant"),
#             NavigationDestinationTemplate(label="Home", icon="home"),
#             NavigationDestinationTemplate(label="Perfil", icon="user"),
#         ],
#         bgcolor="#FFFFFF",
#         height=70,
#     ):
#         super().__init__()
#         self.destinations = destinations
#         self.bgcolor = bgcolor
#         self.height = height

class NavigationBarTemplate(UserControl):
    """
    Classe para criar uma barra de navegação com configurações comuns

    Atributos:
        ATRIBUTO       TIPO                            DEFINIÇÃO
        destinations   (List[NavigationDestination])   lista de destinos de navegação
    """

    def __init__(
        self,
        destinations=[
            NavigationDestinationTemplate(label="Cultura", icon="plant"),
            NavigationDestinationTemplate(label="Home", icon="home"),
            NavigationDestinationTemplate(label="Perfil", icon="user"),
        ],
        bgcolor="#FFFFFF",
        label_behavior=NavigationBarLabelBehavior.ALWAYS_HIDE,
    ):
        super().__init__()
        self.destinations = destinations
        self.bgcolor = bgcolor
        self.label_behavior = label_behavior

    def build(self):
        def navigation_bar_change(e):
    
            # Índice selecionado na barra de navegação
            index = e.control.selected_index
            print("e control:", e.control.selected_index)

        return NavigationBar(
            destinations=self.destinations,
            bgcolor=self.bgcolor,
            label_behavior=self.label_behavior,
            on_change=navigation_bar_change,
            
        )    

class UserNavigationBarTemplate(UserControl):
    def __init__(self):
        super().__init__()
        self.navigation_bar = NavigationBarTemplate()

    def build(self):
        # Função para tratar a mudança de seleção na barra de navegação
        def navigation_bar_change(e):

            # Índice selecionado na barra de navegação
            index = e.control.selected_index
            print("e control:", e.control.selected_index)

        self.navigation_bar.on_change = navigation_bar_change
        self.navigation_bar.margin = -10

        return self.navigation_bar



navigation_bar = NavigationBarTemplate()
