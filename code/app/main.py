import flet as ft

import config.page
import config.routes
import config.firebase


def main(page: ft.Page):

    page.add(config.page.PageConfig())
    page.add(config.routes.RouteConfig())
    # page.add(config.firebase.FirebaseConfig())


ft.app(target=main)
