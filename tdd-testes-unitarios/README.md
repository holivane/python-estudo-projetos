# Projeto ByteBank - Usando Pytest e TDD
Este projeto é um exemplo simples de um programa em python que roda uma Virtual Enviroment (venv) e utiliza o Pytest para testes automatizados. Durante o desenvolvimento dos testes unitários foi utilizada a metodologia TDD (Desenvolvimento Orientado a Testes)

## Requisitos
Antes de exscutar o projeto, verifique se na sua máquina já estão instalados:
- Python (versão 3.8)
- pip

## Configuração

1. Clonar o projeto em sua máquina local com o nome que desejar. Eu sugiro usar *bytebank*.

2. Navegar até a pasta do projeto

3. Criar um ambiente virtual para o projeto, na raiz dele:
```
$ python -m venv venv
```
4. Ativar o ambiente virtual:
```
$ source venv/bin/activate
```
5. Instalar as dependências do projeto:
```
$ pip install -r requirements.txt
```

## Utilização
Para executar o código principal ou os testes, verifique se o ambiente virtual está ativado.

### Rodar o projeto principal
Use o comando:
```
$ python main.py
```
### Executar os testes
Utilize o seguinte comando:
```
$ pytest tests
```

Para ter mais detalhes dos testes você pode usar: **-v**
```
$ pytest tests -v
```

## Estrutura
- codigo
- tests
- .gitignore
- main.py
- README.md
- requirements.txt