from flet import TextField, UserControl
import flet as ft

class TextFieldTemplate(UserControl):
    """
    Classe que cria um objeto TextField com configurações personalizadas.

    Atributos:
        label (str): A descrição do campo de texto.
        value (str): O valor inicial do campo de texto.
        suffix_text (str): O texto que aparece após o valor do campo de texto.
        text_align (TextAlign): O alinhamento do texto dentro do campo de texto.
        text_size (int): O tamanho da fonte do texto do campo de texto.
        read_only (bool): Se o campo de texto é somente leitura ou não.
        width (int): A largura do campo de texto.
        height (int): A altura do campo de texto.
        expand (int): A expansão do campo de texto.
        filled (bool): Se o campo de texto é preenchido ou não.
        bgcolor (str): A cor de fundo do campo de texto.
        border (ft.InputBorder): O estilo da borda do campo de texto.
        border_radius (ft.border_radius): O raio da borda do campo de texto.

    Métodos:
        build(): Cria um objeto TextField com as configurações especificadas no construtor.
    """

    def __init__(
        self,
        label="",
        value="",
        suffix_text="",
        text_align=ft.TextAlign.CENTER,
        text_size=10,
        read_only=True,
        width=400,
        height=70,
        expand=1,
        filled=True,
        bgcolor="#E6E7EB",
        border=ft.InputBorder.NONE,
        border_radius=ft.border_radius.all(100.0),
    ):
        super().__init__()

        self.bgcolor = bgcolor
        self.label = label
        self.border_radius = border_radius
        self.value = value
        self.text_align = text_align
        self.width = width
        self.height = height
        self.expand = expand
        self.suffix_text = suffix_text
        self.border = border
        self.filled = filled
        self.read_only = read_only
        self.text_size = text_size

    def build(self):
        """
        Cria um objeto TextField com as configurações especificadas no construtor

        Retorna: TextField: campo de texto criado
        """
        return TextField(
            label=self.label,
            value=self.value,
            text_align=self.text_align,
            text_size=self.text_size,
            read_only=self.read_only,
            width=self.width,
            height=self.height,
            expand=self.expand,
            suffix_text=self.suffix_text,
            filled=self.filled,
            bgcolor=self.bgcolor,
            border=self.border,
            border_radius=self.border_radius,
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
