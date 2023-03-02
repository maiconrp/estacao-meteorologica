# `DOCS` Aplicação

## Estrutura de Arquivos
A estrutura de arquivos do projeto pode ser organizada da seguinte forma:

```
└── 📂app/
    ├── 📄main.py
    ├── 📄routes.py
    ├── 📂pages/
    │   ├── 📄home.py
    │   ├── 📄login.py
    │   └── ...
    ├── 📂componentes/
    │   ├── 📂botões/
    │   │   ├── 📄ElevatedButton.py
    │   │   └──...
    │   ├── 📂inputs/
    │   │   ├── 📄TextField.py
    │   │   └──...
    │   └── ...
    ├── 📂assets/
    │   ├── 📂icons/
    │   ├── 📂imgs/
    │   ├── 📂fonts/
    ├── 📂utils/
    │   ├── 📄classes.py
    │   ├── 📄equações.py
    ├── 📂firebase/
    │   ├── 📄auth.py
    │   ├── 📄config.py
    │   ├── 📄db.py
    ├── 📄requirements.txt
    └── 📄README.md

```
<details>
<summary> <h3> Diretórios e Arquivos </h3> </summary>

* 📄 **main.py**:  Arquivo principal, responsável por inicializar e gerenciar a execução do aplicativo.
* 📄 **routes.py**: Arquivo que contém as rotas e suas configurações.. 

* 📂 **pages/**: Este diretório contém os arquivos de cada página do aplicativo.

* 📂 **componentes/**:Este diretório contém os arquivos dos componentes reutilizáveis do aplicativo, como botões, inputs, etc.

* 📂 **assets/**: Arquivos de recursos do aplicativo, como imagens, ícones, etc.

* 📂 **utils/**: Este diretório contém arquivos de utilidade, como classes e funções úteis..
    
* 📂 **firebase/**: Arquivos relacionados à autenticação e comunicação com o Firebase.
    * 📄 **auth.py**: Responsável por lidar com a autenticação do usuário.
    * 📄 **config.py**: Contém configurações de conexão com o Firebase.
    * 📄 **db.py**: Responsável por lidar com a comunicação com o banco de dados do Firebase.
    
* 📄 **requirements.txt**: Dependências do projeto.
* 📄 **README.md**: Este arquivo é o que você está lendo agora e descreve a estrutura de arquivos do projeto.
</details>

## Instalação

### Requisitos
- Git
- Pip
- Python 3.8 ou inferior
- Flet 0.4.2

## Passos

1. Instale o [Git](https://git-scm.com/downloads)
2. Abra o terminal ou Git Bash e digite o seguinte comando:

    ```
    git clone https://github.com/maiconrp/estacao-meteorologica.git
    ```

3. Acesse a pasta test_app

    ```
   cd estacao-meteorologica\code\testes\teste_app
    ```
4. Execute o arquivo install.py
    
    ```
   py install.py
    ```

# Observações
- Certifique-se de estar usando a versão correta do Python e do Flet
- Se precisar de mais informações ou tiver dúvidas, consulte a [documentação oficial do Flet][flet].

[flet]: https://flet.dev/docs/
