# `DOCS` Aplicação

# Estrutura de Arquivos
A estrutura de arquivos do projeto pode ser organizada da seguinte forma:

```md
.
└── 📂app/
    ├── 📂assets/
    │   ├── 📂icons/
    │   ├── 📂imgs/
    │   ├── 📂fonts/
    │   ├── colors.py
    │   └──...
    ├── 📂componentes/
    │   ├── 📂botões/
    │   │   ├── 📄ElevatedButton.py
    │   │   └──...
    │   ├── 📄AlertDialog.py
    │   ├── 📄AppBar.py
    │   ├── 📄Card.py
    │   └── ...
    ├── 📂pages/
    │   ├── 📄home.py
    │   ├── 📄login.py
    │   └── ...
    ├── 📂config
    │   ├── 📄firebase.py
    │   ├── 📄page.py
    │   └── 📄routes.py
    ├── 📂utils/
    │   ├── 📄classes.py
    │   ├── 📄equações.py
    │   └── ...
    ├── 📄README.md
    ├── 📄database.py
    ├── 📄install.py
    ├── 📄main.py
    └── 📄requirements.txt

```
<details>
<summary> <h3> Diretórios e Arquivos </h3> </summary>

* 📂 **assets/**: Arquivos de recursos do aplicativo, como imagens, ícones, etc.
    * 📂 icons/: Este diretório contém ícones.
    * 📂 imgs/: Este diretório contém imagens.
    * 📂 fonts/: Este diretório contém fontes.
    * 📄 colors.py: Arquivo que contém as cores usadas no aplicativo.

* 📂 **componentes/**: Este diretório contém os arquivos dos componentes reutilizáveis do aplicativo, como botões, inputs, etc.

* 📂 **pages/**: Este diretório contém os arquivos de cada página do aplicativo.

* 📂 **config/**: Diretório que contém os arquivos de configuração do aplicativo.
    * 📄 firebase.py: Arquivo que contém as funções relacionadas à autenticação e comunicação com o Firebase.
    * 📄 page.py: Arquivo que contém as funções relacionadas à criação de páginas.
    * 📄 routes.py: Arquivo que contém as funções relacionadas à definição de rotas.
    
* 📂 **utils/**: Este diretório contém arquivos de utilidade, como classes e funções úteis.

* 📄 README.md: Este arquivo é o que você está lendo agora e descreve a estrutura de arquivos do projeto.
* 📄 database.py: Arquivo que contém as funções que lidam com o banco de dados.
* 📄 install.py: Arquivo responsável por instalar as dependências do projeto.
* 📄 main.py: Arquivo principal, responsável por inicializar e gerenciar a execução do aplicativo.
* 📄 requirements.txt: Dependências do projeto.

</details>

## Instalação

### Requisitos
- Git
- Python 3.8 ou inferior
- Pip

### Passos

1. Instale o [Git][git]
2. Abra o terminal ou Git Bash e digite o seguinte comando:

    ```
    git clone https://github.com/maiconrp/estacao-meteorologica.git
    ```

3. Acesse a pasta app

    ```
   cd estacao-meteorologica\code\app
    ```
4. Execute o arquivo [install.py](install.py)
    
    ```
   py install.py
    ```

## Observações
- Certifique-se de estar usando a versão correta do Python
- Se precisar de mais informações ou tiver dúvidas, consulte a documentação oficial da [Flet][flet] ou da [Pyrebase4](pyrebase)

[git]: https://git-scm.com/downloads
[flet]: https://flet.dev/docs/
[pyrebase]: https://github.com/nhorvath/Pyrebase4
