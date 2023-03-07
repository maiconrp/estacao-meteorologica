import flet as ft

from componentes.AppBar import appbar
from componentes.NavigationBar import navigation_bar
from componentes.TextField import pressao, radiacao, temperatura, umidade, vento


class MeteorologiaPage:
    """
    Classe MeteorologiaPage para criar uma página de meteorologia.

    Atributos:
        Nenhum atributo.

    Métodos:
        build() -> ft.View:
            Cria uma View contendo AppBar, uma coluna com campos de texto de pressão, radiação, temperatura,
            umidade e vento e uma NavigationBar, todos configurados com o flet. Retorna a View criada.

    Exemplo de uso:
        meteorologia_page = MeteorologiaPage()
        view = meteorologia_page.build()
    """

    def build():
        """
        Cria uma View contendo AppBar, uma coluna com campos de texto de pressão, radiação, temperatura,
        umidade e vento e uma NavigationBar, todos configurados com o flet. Retorna a View criada.

        Args:
            Nenhum argumento.

        Returns:
            ft.View: View contendo AppBar, coluna com campos de texto e NavigationBar.
        """
        return ft.View(
            "/Meteorologia",
            [
                appbar,
                ft.Column([pressao, radiacao, temperatura, umidade, vento]),
                navigation_bar,
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
