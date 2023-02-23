from flet import NavigationBar, NavigationDestination, icons

import flet as ft

class NavigationBarTemplate:
    """
    Classe para criar uma barra de navegação com configurações comuns
    
    Atributos:
        ATRIBUTO       TIPO                            DEFINIÇÃO
        destinations   (List[NavigationDestination])   lista de destinos de navegação
    """

    def __init__(self, destinations):
        self.destinations = destinations

    def build(self):
        """
        Cria um objeto <NavigationBar> com as configurações especificadas no construtor
        
        Retorna: NavigationBar: barra de navegação criada
        """
        return ft.NavigationBar(destinations=self.destinations)
    
destinations = [
    ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Cultura"),
    ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Home"),
    ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Perfil"),
]

navigation_bar = NavigationBarTemplate(destinations).build()
