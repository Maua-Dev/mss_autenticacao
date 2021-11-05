# Changelog

Toda mudança notável a esse projeto será documentado nesse arquivo.

O formato é baseado em [Mantenha um Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e o projeto mantém [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não publicado]
### Adicionado
- Pasta erros para models
- Models básicos para a geração de tokens
- Pasta erros para usecases
- Usecases iniciais para geracação de tokens
- Pasta erros para repositórios
- Pasta criacao para criação de tokens, baseado no que for pedido.
- docker-compose.yml
- Serviço recuperar senha

### Modificado
- Controller CHTTPGerarToken em relação de como é usado e como chama token.py
- Readme
- main, refatorado alguns problemas
- Resources, com mais recursos.

## [0.0.4] - 2021-08-05
### Adicionado 
- UCCriarJWT
- IGeracaoToken, interface para ter todos os métodos relacionados a criação de tokens

### Modificado
- [RESOURCES.md](./RESOURCES.md), adicionando documentação usada de pyjwt e link referência ao jwt.
- [requirements.txt](./requirements.txt), incluindo pyjwt e pyjwt[crypto], para criar jwt assimétrico.


## [0.0.4] - 2021-08-06
### Adicionado
- Pasta erros em src.usecases para retorar os possíveis erros.

### Modificado
- uc_criar_jwt.py para incluir os erros e retornar o token, caso dê certo.

## [0.0.3] - 2021-08-05
### Adicionado
- Pasta Controladores em src
- Pasta Interfaces em src
- Pasta Repositorios em src
- Pasta Usecases em src
- Pasta Models em src
- Pasta Controladores em tests
- Pasta Interfaces em tests
- Pasta Repositorios em tests
- Pasta Usecases em tests
- Pasta Models em tests


## [0.0.2] - 2021-08-03
### Adicionado
- Esse [CHANGELOG.md](./CHANGELOG.md) para documentar mudanças futuras.
- [CONTRIBUTING.md](./CONTRIBUTING.md) para definir padrões para devs verificarem antes de fazer o pull request. Possível que mude no futuro.

### Modificado
- [README.md](./README.md), convertendo para português devido a padrões definidos e alterando para combinar com o projeto.
- .gitignore para ignorar arquivos .pyc
- Dockerfile seguindo o formato do [mss-gerenciamento-usuários](https://github.com/Maua-Dev/mss-gerenciamento-usuarios/blob/main/Dockerfile)
- [requirements.txt](./requirements.txt) seguindo o formato do [mss-gerenciamento-usuários](https://github.com/Maua-Dev/mss-gerenciamento-usuarios/blob/main/requirements.txt)

## [0.0.1] - 2021-08-03
### Adicionado
- Project start