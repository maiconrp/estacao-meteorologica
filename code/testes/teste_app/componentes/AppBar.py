from flet import AppBar
import flet as ft

appbar = AppBar(
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
)