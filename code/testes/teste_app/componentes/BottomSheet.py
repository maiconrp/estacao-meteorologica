import flet as ft
from flet import *

def main(page: ft.Page):
    page.title = "Estacao Meteorologica"

    # Define a largura e altura da janela
    page.window_width = 385.0
    page.window_height = 704.0

    # Habilita a barra de rolagem da página
    page.scroll = "auto"
    # Define que a janela deve ficar sempre no topo
    page.window_always_on_top = True

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

    bs = BottomSheet(
                Container(
                    bgcolor='white',
                    height=309,
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
                            Card(nome, elevation=4),
                            Card(email, elevation=4),
                            Card(senha, elevation=4),
                            Container(
                                border = border.all(2, 'green'),
                                content = OutlinedButton('Sair')
                                )
                        ],
                        tight=True,
                    ),
                    padding=10,
            ),
            open=True,
        )


    page.overlay.append(bs)
    page.add(ft.ElevatedButton("Display bottom sheet", on_click=show_bs))

ft.app(target=main, assets_dir="assets")