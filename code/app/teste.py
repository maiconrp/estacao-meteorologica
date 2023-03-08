import flet as ft

oi = ft.Text("oi")


class PageConfig(ft.UserControl):
    def did_mount(self):
        self.page.window_width = 385.0
        self.page.window_height = 704.0
        self.page.window_always_on_top = True
        self.page.scroll = "auto"
        self.page.title = "Estacao Meteorologica"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = "light"
        self.page.update()

    def build(self):
        return ft.Container()


def main(page):
    page.add(PageConfig())


ft.app(target=main)
