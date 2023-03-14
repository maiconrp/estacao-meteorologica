from flet import *

def show_bs(e):
    bs.open = True
    bs.update()

class FieldTemplate:
    def __init__(
        self,
        bgcolor='white',
        width=280,
        height=47,
        border_radius=7,
        content=None,
        padding = padding.only(left=12)
        

    ):
        self.bgcolor = bgcolor
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.content = content
        self.padding = padding


    def build(self):
        """
        Cria um objeto TextField com as configurações especificadas no construtor

        Retorna: TextField: campo de texto criado
        """
        return Container(
            bgcolor=self.bgcolor,
            width=self.width,
            height=self.height,
            border_radius=self.border_radius,
            content = self.content,
            padding = self.padding

        )

nome = FieldTemplate(content=Row(
    [
        Image(src=f"assets/icons/perfil_green.svg", width=17, height=17),
        Text('Victor Henrique Fonteles Silva', weight=FontWeight.W_600, size=16),
    ])).build()

email = FieldTemplate(content=Row(
    [
        Image(src=f"assets/icons/email.svg", width=17, height=17),
        Text('victorsilva@gmail.com', weight=FontWeight.W_600, size=16),
    ])).build()

senha = FieldTemplate(content=Row(
    [
        Image(src=f"assets/icons/cadeado.svg", width=20, height=20),
        Text('******', weight=FontWeight.W_600, size=16),
    ])
    ).build()

logout = Container(
    width = 280,
    height = 47,
    bgcolor = 'white',
    alignment=alignment.center,
    border_radius=6,
    on_click='Clicked',
    border = border.all(1, color='#00D154'),
    content = Text('SAIR', color='#00D154', size=14, weight=FontWeight.W_600),
)

bs = BottomSheet(
            Container(
                bgcolor='white',
                height=329,
                width=329,
                content = Column(horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls = [
                        Container(
                        margin=margin.only(bottom=-14),
                        content=Text(
                                'Olá produtor', size=20, color='#000000', weight=FontWeight.W_700
                            ),
                        ),
                        Text('Este é o seu perfil', size=13, color='#000000'),
                        Card(nome, elevation=8),
                        Card(email, elevation=8),
                        Card(senha, elevation=8),
                        logout,
                    ],
                    tight=True,
                ),
                padding=10,
        ),
        open=True,
    )


page.overlay.append(bs)
page.add(ft.ElevatedButton("Display bottom sheet", on_click=show_bs))