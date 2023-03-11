import flet as ft
from flet import *

"""class AlertDialogTemplate(ft.UserControl):
    def __init__(
        self,
        modal=False,
        title=None,
        title_padding=None,
        content=None,
        content_padding=None,
        actions=None,
        actions_padding=None,
        actions_alignment="center",
        shape=None,
        on_dismiss=None,
    ):
        def on_close(self, e):
            self.open = False
            self.page.update()
            print("close")

        def on_open(self, e):
            self.page.dialog = dlg_modal
            self.open = True
            self.page.update()
            print("open")

        super().__init__()
        self.page = page
        self.modal = modal
        self.title = title
        self.title_padding = title_padding
        self.content = content
        self.content_padding = content_padding
        self.actions = actions
        self.actions_padding = actions_padding
        self.actions_alignment = actions_alignment
        self.shape = shape
        self.on_dismiss = on_dismiss
        self.on_open = on_open
        self.on_close = on_close

    def build(self):

        actions = []
        for action in self.actions:
            if isinstance(action, str):
                actions.append(ft.TextButton(action, on_click=close))
            else:
                actions.append(action)
        self.page.add(
            ft.ElevatedButton("Open modal dialog", on_click=open),
        )
        return ft.AlertDialog(
            modal=self.modal,
            title=ft.Text(self.title),
            title_padding=self.title_padding,
            content=ft.Text(self.content),
            content_padding=self.content_padding,
            actions=actions,
            actions_padding=self.actions_padding,
            actions_alignment=self.actions_alignment,
            shape=self.shape,
            on_dismiss=self.on_dismiss,
        )
"""


class TextFieldTemplate:
    def __init__(
        self,
        bgcolor="#E6E7EB",
        width=50,
        height=50,
        border_radius=7,
        read_only=True,
        label="Field",
        value="Info",
        border=InputBorder.NONE,
    ):
        self.bgcolor = bgcolor
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.read_only = read_only
        self.label = label
        self.value = value
        self.border = border

    # top_view = self.page.views[-1]

    def build(self):
        """
        Cria um objeto TextField com as configurações especificadas no construtor

        Retorna: TextField: campo de texto criado
        """
        return TextField(
            bgcolor=self.bgcolor,
            width=self.width,
            height=self.height,
            border_radius=self.border_radius,
            read_only=self.read_only,
            label=self.label,
            value=self.value,
            border=self.border,
        )


tipo = TextFieldTemplate(width=300, label="Tipo", value="Milho").build()

data = TextFieldTemplate(width=110, label="Data de plantio", value="25/08/2022").build()

area = TextFieldTemplate(width=110, label="Área", value="3500m²").build()

vazao = TextFieldTemplate(width=300, label="Vazão", value="1300 L/h").build()

tempo_ant = TextFieldTemplate(width=70, label="Anterio", value="4h").build()

tempo_atu = TextFieldTemplate(width=70, label="Atual", value="3h").build()

economia = TextFieldTemplate(
    width=70, bgcolor="#00D154", label="Economia", value="27%"
).build()

estagio = TextFieldTemplate(width=90, label="Estágio", value="Maturação").build()

duracao = TextFieldTemplate(width=65, label="Duração", value="27 dias").build()

kc = TextFieldTemplate(width=65, label="Kc", value="1.7").build()

dlg_cultura = ft.AlertDialog(
    content=Container(
        bgcolor="white",
        height=390,
        width=270,
        content=Column(
            controls=[
                Row(
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Container(
                            content=Image(
                                src=f"assets/icons/corn.png",
                                width=170,
                                height=170,
                            ),
                            margin=margin.only(right=-130, bottom=-60, top=-60),
                        ),
                        Text(
                            "Milho",
                            color="#000000",
                            size=28,
                            weight=FontWeight.W_800,
                        ),
                    ],
                ),
                tipo,
                Row(
                    controls=[
                        data,
                        area,
                    ]
                ),
                vazao,
                Container(
                    content=Text(
                        "Tempo de irrigação",
                        color="#000000",
                        size=13,
                        weight=FontWeight.W_600,
                    )
                ),
                Row(
                    controls=[
                        tempo_ant,
                        tempo_atu,
                        economia,
                    ]
                ),
                Container(
                    content=Text(
                        "Desenvolvimento",
                        color="#000000",
                        size=13,
                        weight=FontWeight.W_600,
                    )
                ),
                Row(
                    controls=[
                        estagio,
                        duracao,
                        kc,
                    ]
                ),
            ]
        ),
    )
)
