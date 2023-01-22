# `DOCS` Aplicação

# Estrutura de Arquivos
A estrutura de arquivos do projeto pode ser organizada da seguinte forma:

```md
.
├── app/
│   ├── main.py
│   ├── pages/
│   │   ├── home.py
│   │   ├── login.py
│   │   └── ...
│   ├── components
│   │   ├── button.py
│   │   ├── textfield.py
│   │   └── ...
│   ├── assets/
│   ├── utils/
│   │   ├── models.py
│   │   ├── routes.py
│   ├── firebase/
│   │   ├── auth.py
│   │   ├── db.py
│   ├── config/
│   │   ├── settings.py
│   │   └── firebase.py
│   ├── requirements.txt
|   └── README.md


```

### Diretórios e Arquivos

*  **main.py**:  arquivo principal, responsável por inicializar e gerenciar a execução do aplicativo.

* **pages/**: Arquivos relacionados às páginas do aplicativo. Cada arquivo dentro deste diretório representa uma página diferente do aplicativo. Por exemplo, "home.py" representa a página inicial do aplicativo e "settings.py" representa a página de configurações.

*  **components/**: Arquivos relacionados aos componentes do aplicativo. Cada arquivo dentro deste diretório representa um componente diferente do aplicativo. Por exemplo, "button.py" representa o componente de botão e "textfield.py" representa o componente de campo de texto.

*  **assets/**: Arquivos de recursos do aplicativo, como imagens, ícones, etc.

*  **utils/**: Arquivos de utilitários do aplicativo, como funções de ajuda, configurações, etc.
    *  **models.py**: Responsável por lidar com a lógica de negócios e comunicação com o banco de dados.
    *  **routes.py**: Responsável por configurar as rotas da aplicação.  
    
*  **firebase/**: Arquivos relacionados à autenticação e comunicação com o Firebase.
    *  O arquivo "auth.py" é responsável por lidar com a autenticação do usuário.
    *  O arquivo "db.py" é responsável por lidar com a comunicação com o banco de dados do Firebase.
    
*  **config/**: Arquivos de configurações do aplicativo.
    *  **settings.py**" contém configurações gerais do aplicativo.
    *  **db_config.py**" contém configurações de conexão com o banco
