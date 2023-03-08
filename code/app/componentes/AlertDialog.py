import flet as ft


class AlertDialogTemplate(ft.UserControl):
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
