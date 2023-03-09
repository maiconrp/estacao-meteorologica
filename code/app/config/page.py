import flet as ft
from flet import UserControl, Theme
import assets.colors
import assets.fonts.config

class PageConfig(UserControl):
    def did_mount(self):
        """
        Configura as propriedades da página.
        """
        # Define o título da página
        self.page.title = "Estacao Meteorologica"

        # Define a largura e altura da janela
        self.page.window_width = 385.0
        self.page.window_height = 704.0

        # Habilita a barra de rolagem da página
        self.page.scroll = "auto"
        # Define que a janela deve ficar sempre no topo
        self.page.window_always_on_top = True
        # Define a posição horizontal do conteúdo na janela
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Define o modo e o tema da página
        self.page.theme_mode = "light"
        self.page.theme = ft.theme.Theme(
            color_scheme_seed=assets.colors.BACKGROUND2, use_material3=True
        )
        # Atualiza a página
        self.page.fonts = assets.fonts.config.load()
        self.page.update()
        print(self.page.fonts)

    def build(self):
        """
        Retorna um container vazio.
        """
        return ft.Container()
