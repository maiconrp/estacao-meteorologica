import flet as ft
from flet import (
    alignment,
    AppBar,
    FilledTonalButton,
    FontWeight,
    Icon,
    Row,
    Text,
    UserControl,
    Column,
    Container,
    MainAxisAlignment,
    margin,
    Page,
)
import assets.colors

def update(e):
    page = ft.Page
    page.update(self)

estacao = Container(
    width=70,
    height=29,
    margin=ft.margin.only(right=25.0, left=-50),
    content=Container(
        bgcolor=assets.colors.WIDGET,
        padding=ft.padding.symmetric(horizontal=10),
        border_radius=100,
        content=Row(
            spacing=3,
            controls=[
                Text(
                    value="Estação", color="#000000", size=10, weight=FontWeight.W_600
                ),
                Icon("settings", color=assets.colors.PRIMARY_GREEN, size=10),
            ],
        ),
    ),
)

update= Container(
    width=29,
    height=29,
    alignment = alignment.center,
    on_click=update,
    content=Container(
        bgcolor=assets.colors.WIDGET,
        border_radius=100,
        padding=ft.padding.symmetric(horizontal=3),
        content=Row(
            controls=[
                Icon(name=ft.icons.UPDATE, color=assets.colors.PRIMARY_GREEN, size=22),
            ],
        ),
    ),
)




class AppBarTemplate(AppBar):
    """
    Classe para criar uma barra de aplicativo com configurações comuns

    Atributos:
        ATRIBUTO       TIPO        DEFINIÇÃO                                                             DEFAULT
        title          (Any):      Título da barra de aplicativo                                           (None)
        bgcolor        (Color):    Cor de fundo da barra de aplicativo                                     (colors.PRIMARY)
        actions        (list):     Lista de elementos a serem exibidos à direita da barra de aplicativo     (None)
    """

    def __init__(
        self,
        title=Container(
            content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    Column(
                        controls=[
                            Text(
                                value="Olá, Victor",
                                color="#000000",
                                size=20,
                                weight=FontWeight.W_700,
                                font_family="Poppins Bold",
                            ),
                            Text(
                                value="Quinta, 26 de janeiro",
                                color="#000000",
                                size=10,
                                font_family="Poppins Regular",
                            ),
                        ],
                        spacing=3,
                    ),
                    update,
                    estacao,
                ]
            ),
            margin=margin.only(left=20, bottom=10),    
        ),
        bgcolor="transparent",
    ):
        """
        Construtor da classe AppBarTemplate. Define os atributos title, bgcolor e actions da AppBar.

        Atributos:
        ATRIBUTO       TIPO        DEFINIÇÃO                                                             DEFAULT
        title          (Any):      Título da barra de aplicativo                                           (None)
        bgcolor        (Color):    Cor de fundo da barra de aplicativo                                     (colors.PRIMARY)
        actions        (list):     Lista de elementos a serem exibidos à direita da barra de aplicativo     (None)

        Returns:
            Nenhum retorno.
        """
        super().__init__()
        self.title = title
        self.bgcolor = bgcolor


appbar = AppBarTemplate()
