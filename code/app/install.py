import os
import platform
import subprocess
import sys
from pathlib import Path


def bem_vind():
    """
    Função que escreve uma mensagem de bem vindo(a).
    A msg é uma lista que é printada usando o metodo de descompactação do python
    """
    msg = [
        "\n[NOTA]\n",
        "#  Sejam bem-vindos ao projeto!\n",
        "#  Gostaríamos de informar que a versão atual do código está na fase de testes,",
        "#  o que significa que pode haver alguns bugs e problemas de funcionamento.\n",
        "#  Pedimos que, caso encontrem algum problema ou tenham sugestões de melhoria,",
        "#  não hesitem em entrar em contato conosco. Estamos sempre abertos a feedbacks ",
        "#  construtivos que possam nos ajudar a aprimorar o nosso produto.\n",
        "#  Agradecemos desde já pelo interesse em nosso projeto e contamos com a colaboração de todos para torná-lo ainda melhor.\n",
        "#  Atenciosamente,",
        "#  A equipe de desenvolvimento.!" "\n\nInstalação:",
    ]

    print(*msg, sep="\n")


def print_step(msg: str, status: Optional[str] = "info"):
    """
    Função que imprime msg de texto de forma personalizada
    """
    color = {
        "success": "\033[1;32m",  # verde
        "error": "\033[1;31m",  # vermelho
        "info": "\033[1;37m",  # branco
    }
    end_color = "\033[0m"

    status_msg = {
        "success": "[OK]",
        "error": "[X]",
        "info": "[I]",
    }

    if status == "info":
        print(f"{status_msg[status]} {msg}")
    else:
        print(f"{color[status]}{status_msg[status]} {msg}{end_color}")


def create_virtual_env():
    """
    Cria um ambiente virtual para o projeto.
    """
    print_step("Configurando ambiente virtual...")

    python_cmd = "python" if platform.system() == "Windows" else "python3"
    venv_cmd = (
        "py -3.8 -m venv" if platform.system() == "Windows" else "python3.8.6 -m venv"
    )

    venv_path = Path("venv")
    if not venv_path.exists():
        create_venv_cmd = f"{venv_cmd} venv"
        try:
            subprocess.check_call(create_venv_cmd, shell=True)
            print_step("Ambiente virtual criado com sucesso!", "success")
        except subprocess.CalledProcessError as e:
            print_step(f"Erro ao criar ambiente virtual. {e}", "error")
            sys.exit(1)
    else:
        print_step("Ambiente virtual já existe.", "info")


def activate_virtual_env():
    """
    Ativa o ambiente virtual criado e retorna o comando de ativação.
    """
    print_step("Ativando ambiente virtual...")

    venv_path = Path("venv")
    if not venv_path.exists():
        print_step("O ambiente virtual não existe. Crie-o antes de ativá-lo.", "error")
        return None

    if platform.system() == "Windows":
        activate_path = os.path.join("venv", "Scripts", "activate.bat")
        activate_cmd = f"{activate_path} &&"
    else:
        activate_path = os.path.join("venv", "bin", "activate")
        activate_cmd = f"source {activate_path} &&"

    return activate_cmd


def install_dependencies():
    """
    Instala as dependências listadas no arquivo requirements.txt
    """
    activate_cmd = activate_virtual_env()

    print_step("Instalando dependências...")

    try:
        install_requirements_cmd = f"{activate_cmd} pip install -q --disable-pip-version-check -r requirements.txt"
        subprocess.check_call(install_requirements_cmd, shell=True)
        print_step("Dependências instaladas com sucesso!", "success")
    except subprocess.CalledProcessError as e:
        print_step(f"Erro ao instalar dependências. {e}", "error")
        sys.exit(1)


def run_main():
    """
    Executa o arquivo main.py
    """

    print_step("Executando main.py...")

    try:
        run_main_cmd = f"python main.py"
        subprocess.check_call(run_main_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print_step(f"Erro ao executar main.py. {e}", "error")
        sys.exit(1)


def main():
    """
    Função principal.
    """
    bem_vind()
    create_virtual_env()
    install_dependencies()
    run_main()


if __name__ == "__main__":
    main()
