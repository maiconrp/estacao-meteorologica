from flet import TextField, TextAlign


class TextFieldTemplate:
    """
    Classe para criar campos de texto com configurações comuns

    Atributos:
        ATRIBUTO    TIPO        DEFINIÇÃO                               DEFAULT
        label       (str)       Descrição do campo de texto             ("Texto")
        value       (int)       Valor inicial do campo de texto         (0)
        text_align  (TextAlign) Alinhamento do texto dentro do campo    (TextAlign.CENTER)
        width       (int)       Largura do campo de texto               (175)
        suffix_text (str)       Texto que aparece após o valor          ("")
    """

    def __init__(self, label="Texto", value=0, text_align=TextAlign.CENTER, width=175, suffix_text=""):
        self.label = label
        self.value = value
        self.text_align = text_align
        self.width = width
        self.suffix_text = suffix_text

    def build(self):
        """
        Cria um objeto TextField com as configurações especificadas no construtor

        Retorna: TextField: campo de texto criado
        """
        return TextField(
            label=self.label,
            value=self.value,
            text_align=self.text_align,
            width=self.width,
            suffix_text=self.suffix_text
        )


# Criação de campos de texto com configurações comuns


pressao = TextFieldTemplate(
    label="Pressão",                # Descrição
    suffix_text="hPa"               # texto atras do valor, complemento
).build()

radiacao = TextFieldTemplate(
    label="Radiacao",
    suffix_text="W/m²"
).build()

temperatura = TextFieldTemplate(
    label="Temperatura",
    suffix_text="°C"
).build()

umidade = TextFieldTemplate(
    label="Umidade",
    suffix_text="%"
).build()

vento = TextFieldTemplate(
    label="Vento",
    suffix_text="km/h"
).build()
