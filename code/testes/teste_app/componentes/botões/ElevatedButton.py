import flet as ft

def elevated_button_template(autofocus=False, bgcolor=ft.colors.PRIMARY, color=ft.colors.WHITE, content=None, elevation=2, icon=None, icon_color=ft.colors.PRIMARY, style=None, text="Button", tooltip=None):
    return ft.ElevatedButton(autofocus=autofocus, bgcolor=bgcolor, color=color, content=content, elevation=elevation, icon=icon, icon_color=icon_color, style=style, text=text, tooltip=tooltip)

HomeButton = elevated_button_template(text="Estou em home")
LoginButton = elevated_button_template(text="Estou em login")

ElevatedButton = elevated_button_template(text="Go to Login")
ElevatedButton2 = elevated_button_template(text="Go to HOME")