import flet as ft

# class TextFieldTemplate:
#     def __init__(self, label="Texto", value=0, text_align=ft.TextAlign.CENTER, width=175, suffix_text=""):
#         self.label=label
#         self.value=value
#         self.text_align=text_align
#         self.width=width
#         self.suffix_text=suffix_text

#     def new(self):
#         label=self.label
#         value=self.value
#         text_align=self.text_align
#         width=self.width
#         suffix_text=self.suffix_text
#         return ft.TextField(label=label, value=value, text_align=text_align, width=width, suffix_text=suffix_text)


def text_fiel_template(label="Texto", value=0, text_align=ft.TextAlign.CENTER, width=175, suffix_text=""):
    return ft.TextField(label=label, value=value, text_align=text_align, width=width, suffix_text=suffix_text)

pressao = text_fiel_template(
    label="Pressão",                # Descrição
    suffix_text="hPa"               # texto atras do valor, complemento
    )

radiacao = text_fiel_template(
    label="Radiacao",
    suffix_text="W/m²"
    )

temperatura = text_fiel_template(
    label="Temperatura",
    suffix_text="°C"
    )

umidade = text_fiel_template(
    label="Umidade",
    suffix_text="%"
    )

vento = text_fiel_template(
    label="Vento",
    suffix_text="km/h"
)
