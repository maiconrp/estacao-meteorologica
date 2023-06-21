from flet import TextField, TextAlign, UserControl


class TextFieldTemplate(UserControl):
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

    def __init__(
        self,
        bgcolor="white",
        label="Texto",
        border_radius=25,
        value=0,
        text_align=TextAlign.CENTER,
        width=400,
        height=70,
        suffix_text="",
    ):
        super().__init__()
        self.label = label
        self.value = value
        self.text_align = text_align
        self.width = width
        self.suffix_text = suffix_text

    def on_change(self):
        self.update()

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
            suffix_text=self.suffix_text,
            on_change=lambda _: self.update(),
        )


# Criação de campos de texto com configurações comuns


pressao = TextFieldTemplate(
    label="Pressão", suffix_text="hPa"  # Descrição  # texto atras do valor, complemento
)

radiacao = TextFieldTemplate(label="Radiacao", suffix_text="W/m²")

temperatura = TextFieldTemplate(label="Temperatura", suffix_text="°C")

umidade = TextFieldTemplate(label="Umidade", suffix_text="%")

vento = TextFieldTemplate(label="Vento", suffix_text="km/h")
