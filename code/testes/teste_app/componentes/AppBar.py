from flet import AppBar
import flet as ft

class AppBarTemplate:
    """
    Classe para criar uma barra de aplicativo com configurações comuns

    Atributos:
        ATRIBUTO       TIPO        DEFINIÇÃO                                                             DEFAULT
        leading        (Any):      Elemento a ser exibido à esquerda da barra de aplicativo                 (None)
        leading_width  (int):      Largura do elemento à esquerda                                          (None)
        title          (Any):      Título da barra de aplicativo                                           (None)
        center_title   (bool):     Se o título está centralizado na barra de aplicativo                     (True)
        bgcolor        (Color):    Cor de fundo da barra de aplicativo                                     (ft.colors.PRIMARY)
        actions        (list):     Lista de elementos a serem exibidos à direita da barra de aplicativo     (None)
    """

    def __init__(
        self,
        leading=None,
        leading_width=None,
        title=None,
        center_title=True,
        bgcolor=ft.colors.PRIMARY,
        actions=None
    ):
        self.leading = leading
        self.leading_width = leading_width
        self.title = title
        self.center_title = center_title
        self.bgcolor = bgcolor
        self.actions = actions

    def build(self):
        """
        Cria um objeto <AppBar> com as configurações especificadas no construtor

        Retorna: AppBar: barra de aplicativo criada
        """
        return ft.AppBar(
            leading=self.leading,
            leading_width=self.leading_width,
            title=self.title,
            center_title=self.center_title,
            bgcolor=self.bgcolor,
            actions=self.actions
        )

appbar = AppBarTemplate(
    leading=ft.Icon(ft.icons.PALETTE),
    leading_width=40,
    title=ft.Text("Estação Metereológica"),
    center_title=False,
    bgcolor=ft.colors.GREEN,
    actions=[
        ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        ft.IconButton(ft.icons.FILTER_3),
        ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Item 1"),
                ft.PopupMenuItem(),  # divider
                ft.PopupMenuItem(
                    text="Checked item", checked=False
                ),
            ]
        ),
    ],
).build()

