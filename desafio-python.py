import requests

class UsuarioGithub:
    """
    Classe para representar os dados de um usuário do Github.

    Atributos:
    - nome: str
        O nome do usuário do Github.
    - url_perfil: str
        A URL para o perfil do usuário.
    - repositorios_publicos: int
        O número de repositórios públicos do usuário.
    - seguidores: int
        O número de seguidores do usuário.
    - seguindo: int
        O número de pessoas que o usuário está seguindo.
    """

    def __init__(self, nome: str, url_perfil: str, repositorios_publicos: int, seguidores: int, seguindo: int):
        """
        Construtor para instanciar a classe UsuarioGithub.

        Parâmetros:
        - nome: str
            O nome do usuário do Github.
        - url_perfil: str
            A URL para o perfil do usuário.
        - repositorios_publicos: int
            O número de repositórios públicos do usuário.
        - seguidores: int
            O número de seguidores do usuário.
        - seguindo: int
            O número de pessoas que o usuário está seguindo.
        """
        self.nome = nome
        self.url_perfil = url_perfil
        self.repositorios_publicos = repositorios_publicos
        self.seguidores = seguidores
        self.seguindo = seguindo

def obter_usuario_github(nome_usuario: str) -> UsuarioGithub:
    """
    Função para obter os dados de um usuário do Github usando a API do Github.

    Parâmetros:
    - nome_usuario: str
        O nome de usuário do Github.

    Retorna:
    - UsuarioGithub:
        O objeto UsuarioGithub contendo os dados do usuário.
    """
    # Fazendo uma solicitação GET para a API do Github para obter os dados do usuário
    resposta = requests.get(f"https://api.github.com/users/{nome_usuario}")

    # Verificando se a solicitação foi bem-sucedida
    if resposta.status_code == 200:
        # Analisando a resposta JSON
        dados_usuario = resposta.json()

        # Extraindo os dados necessários da resposta
        nome = dados_usuario.get("nome")
        url_perfil = dados_usuario.get("url_perfil")
        repositorios_publicos = dados_usuario.get("repositorios_publicos")
        seguidores = dados_usuario.get("seguidores")
        seguindo = dados_usuario.get("seguindo")

        # Criando um objeto UsuarioGithub com os dados extraídos
        usuario_github = UsuarioGithub(nome, url_perfil, repositorios_publicos, seguidores, seguindo)

        return usuario_github
    else:
        # Se a solicitação não foi bem-sucedida, lança uma exceção
        raise Exception(f"Falha ao obter os dados do usuário. Código de status: {resposta.status_code}")

def obter_repositorios_usuario(nome_usuario: str) -> dict:
    """
    Função para obter os repositórios de um usuário do Github.

    Parâmetros:
    - nome_usuario: str
        O nome de usuário do Github.

    Retorna:
    - dict:
        Um dicionário contendo os nomes dos repositórios do usuário como chaves e as URLs dos repositórios como valores.
    """
    # Fazendo uma solicitação GET para a API do Github para obter os repositórios do usuário
    resposta = requests.get(f"https://api.github.com/users/{nome_usuario}/repos")

    # Verificando se a solicitação foi bem-sucedida
    if resposta.status_code == 200:
        # Analisando a resposta JSON
        dados_repositorios = resposta.json()

        # Criando um dicionário vazio para armazenar os nomes e URLs dos repositórios
        repositorios = {}

        # Extraindo os nomes e URLs dos repositórios da resposta
        for dados_repo in dados_repositorios:
            nome_repo = dados_repo.get("name")
            url_repo = dados_repo.get("html_url")
            repositorios[nome_repo] = url_repo

        return repositorios
    else:
        # Se a solicitação não foi bem-sucedida, lança uma exceção
        raise Exception(f"Falha ao obter os repositórios do usuário. Código de status: {resposta.status_code}")

def gerar_relatorio_usuario(usuario: UsuarioGithub, repositorios: dict):
    """
    Função para gerar um relatório de usuário em um arquivo de texto.

    Parâmetros:
    - usuario: UsuarioGithub
        O objeto UsuarioGithub contendo os dados do usuário.
    - repositorios: dict
        Um dicionário contendo os nomes dos repositórios do usuário como chaves e as URLs dos repositórios como valores.
    """
    # Criando o nome do arquivo de relatório com base no nome de usuário
    nome_arquivo_relatorio = f"{usuario.nome}.txt"

    # Abrindo o arquivo de relatório em modo de escrita
    with open(nome_arquivo_relatorio, "w") as arquivo_relatorio:
        # Escrevendo os dados do usuário no arquivo de relatório
        arquivo_relatorio.write(f"Nome do Usuário: {usuario.nome}\n")
        arquivo_relatorio.write(f"URL do Perfil do Usuário: {usuario.url_perfil}\n")
        arquivo_relatorio.write(f"Número de Repositórios Públicos: {usuario.repositorios_publicos}\n")
        arquivo_relatorio.write(f"Número de Seguidores: {usuario.seguidores}\n")
        arquivo_relatorio.write(f"Número de Pessoas que o Usuário Está Seguindo: {usuario.seguindo}\n\n")

        # Escrevendo os dados dos repositórios no arquivo de relatório
        arquivo_relatorio.write("Repositórios:\n")
        for nome_repo, url_repo in repositorios.items():
            arquivo_relatorio.write(f"- {nome_repo}: {url_repo}\n")

    print(f"Relatório do usuário gerado com sucesso. Nome do arquivo: {nome_arquivo_relatorio}")

# Exemplo de uso:

# Passo 1: Criar um objeto UsuarioGithub
usuario = UsuarioGithub("João Silva", "https://github.com/joaosilva", 10, 100, 50)

# Passo 2: Obter os dados do usuário usando a API do Github
usuario_github = obter_usuario_github("joaosilva")

# Passo 3: Obter os repositórios do usuário usando a API do Github
repositorios = obter_repositorios_usuario("joaosilva")

# Passo 4: Gerar o relatório do usuário
gerar_relatorio_usuario(usuario_github, repositorios)
