# MSS - Autenticação
[![codecov](https://codecov.io/gh/Maua-Dev/back_fastAPI_template/branch/main/graph/badge.svg?token=M16VBNGBR3)](https://app.codecov.io/gh/Maua-Dev/mss_autenticacao)

Microsserviço para o sistema de Autenticação, usando JWT 


# Instalação

Comece ao clonar o repositório do modo que achar mais adequado.

### Criar um ambiente virtual python:
    py -m venv venv

### Ativar ambiente virtual (windows)
    venv\Scripts\activate

### Instalar pacotes necessários
    pip install -r requirements.txt

# Uso:

### Desenvolvimento com Docker Composer

Para construir a imagem:
    
    docker-compose build

Para subir o container:

    docker-compose up

### Iniciar server

    uvicorn src.main:app --reload

### Rodar testes

    pytest

# Autores
## Grupo Back-end

    Nome - Github username
# Contribuições
Sendo um projeto fechado para alunos da faculdade Mauá, apenas os alunos podem contribuir para o projeto. 
Para mudanças, edições e outros, ver o arquivo [CONTRIBUTING.md](./CONTRIBUTING.md)

# Licença
No momento, não há licença. 