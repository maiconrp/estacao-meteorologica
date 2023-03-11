import flet as ft

import config.page
import config.routes
import config.firebase

from componentes.NavigationBar import navigation_bar


def main(page: ft.Page):

    navigation_bar.page = page

    config.routes.RouteConfig(page)
    config.page.PageConfig(page)
    # firebase = config.firebase.FirebaseConfig(page)


ft.app(target=main)
