import flet as ft
from flet import *

class DialogTemplateCadastro(ft.UserControl):
    def __init__(
        self,
        modal=False,
        content=None,
        content_padding=padding.only(bottom=-10, top=10, left=0, right=0),
        actions=None,
        actions_padding=None,
        actions_alignment="center",
        shape=RoundedRectangleBorder(radius=10),
        on_dismiss=None,
    ):
        def on_close(self, e):
            self.open = False
            self.page.update()
            print("close")

        def on_open(self, e):
            self.page.dialog = dlg_cadastro
            self.open = True
            self.page.update()
            print("open")

        super().__init__()
        self.page = page
        self.modal = modal
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
        """for action in self.actions:
            if isinstance(action, str):
                actions.append(ft.TextButton(action, on_click=close))
            else:
                actions.append(action)
        self.page.add(
            ft.ElevatedButton("Open modal dialog", on_click=open),
        )"""
        return ft.AlertDialog(
            modal=self.modal,
            content=self.content,
            content_padding=self.content_padding,
            actions=actions,
            actions_padding=self.actions_padding,
            actions_alignment=self.actions_alignment,
            shape=self.shape,
            on_dismiss=self.on_dismiss,
        )

class TextFieldTemplate(UserControl):
    def __init__(
        self,
        border_radius=6,
        filled=True,
        border_color=colors.TRANSPARENT,
        bgcolor="#F1F4FA",
        width=241,
        height=40,
        label="Field",
        label_style=TextStyle(size=12, color='#1c2439', weight=FontWeight.W_400),
        text_style = TextStyle(size=12, color='#1c2439'),
    ):
        super().__init__()
        self.filled = filled
        self.border_color = border_color
        self.bgcolor = bgcolor
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.label = label
        self.label_style = label_style
        self.text_style = text_style

    # top_view = self.page.views[-1]

    def build(self):
        """
        Cria um objeto TextField com as configurações especificadas no construtor

        Retorna: TextField: campo de texto criado
        """
        return TextField(
            filled = self.filled,
            border_color = self.border_color,
            bgcolor=self.bgcolor,
            width=self.width,
            height=self.height,
            border_radius=self.border_radius,
            label=self.label,
            label_style = self.label_style,
            text_style = self.text_style,
        )

data_plantio = TextFieldTemplate(
    label='Data de plantio'
).build()

area = TextFieldTemplate(
    label='Área'
).build()

vazao_gotejador = TextFieldTemplate(
    width=140, label='Vazão do gotejador'
).build()

unidade_vazao = Dropdown(
    options=[
        dropdown.Option("L/min"),
        dropdown.Option("L/h"),
    ],
    label='Vazão',
    width=88,
    height=40,
    border_radius=6,
    text_style = TextStyle(size=11, color='#1c2439'),
    label_style = TextStyle(size=11, color='#1c2439'),
    filled=True,
    border_color=colors.TRANSPARENT,
    bgcolor='#F1F4FA',
)

tipo = Dropdown(
    options=[
        dropdown.Option("Milho"),
        dropdown.Option("Mandioca"),
        dropdown.Option("Acerola"),
        dropdown.Option("Pitamba"),
    ],
    label='Tipo',
    width=241,
    height=40,
    text_style = TextStyle(size=11, color='#1c2439'),
    label_style = TextStyle(size=11, color='#1c2439'),
    border_radius=6,
    filled=True,
    border_color=colors.TRANSPARENT,
    bgcolor='#F1F4FA',
)

title_cadastrar = Text('Cadastro de cultura', color='#000000', size=17, weight=FontWeight.W_700)

text_cadastrar = Text('Preencha os campos abaixo para\ncadastrar sua cultura.', color='#000000', size=13)

btn_cadastrar = Container(
    width = 240,
    height = 40,
    bgcolor = '#00D154',
    alignment=alignment.center,
    border_radius=6,
    on_click='Clicked',
    content = Text('CADASTRAR', color='white', size=11, ),
)

dlg_cadastro = DialogTemplateCadastro(
    content=Container(
        padding=padding.only(top=8, left=15, right=15, bottom=15),
        width=270,
        height=356,
        bgcolor='white',
        content = Column(alignment=MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Container(
                    alignment = alignment.top_left,
                    content = title_cadastrar,   
                ),
                    Container(
                    alignment = alignment.top_left,
                    margin=margin.only(bottom=10),
                    content = text_cadastrar,   
                ),
                tipo,
                data_plantio,
                area,
                Row(
                    controls = [
                        vazao_gotejador,
                        unidade_vazao,
                    ]
                ),
                Card(
                    elevation=4,
                    content=btn_cadastrar,
                ),
            ]
        )
    ),
).build()
    
