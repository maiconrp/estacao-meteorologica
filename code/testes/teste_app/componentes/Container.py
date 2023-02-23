
import flet as ft
from flet import UserControl


class ContainerTemplate(UserControl):
    def __init__(
        self, 
        content=ft.Text("Non clickable"),
        margin=None,
        padding=None,
        alignment=None,
        bgcolor=None,
        width=None,
        height=None,
        border_radius=None
    ):

        self.content=content
        self.margin=margin
        self.padding=padding
        self.alignment=alignment
        self.bgcolor=bgcolor

        self.border_radius=border_radius


    def build(self):
        return ft.Container(
            content=self.content,
            margin=self.margin,
            padding=self.padding,
            alignment=self.alignment,
            bgcolor=self.bgcolor,
            width=self.width,
            height=self.height,
            border_radius=self.borderradius,
        )

Irrigacao = ContainerTemplate(
    margin=10,
    padding=10,
    alignment=ft.alignment.center,
    bgcolor=ft.colors.AMBER,
    width=150,
    height=150,
    border_radius=10,
)

Evapotranspiracao = ContainerTemplate(
                    content=ft.Text("Non clickable"),
                    bgcolor=ft.colors.AMBER,
                )

Economia = ContainerTemplate(
                    content=ft.Text("Non clickable"),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                )

"""            
            ft.Row(
            [
                ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Clickable without Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable transparent with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
"""