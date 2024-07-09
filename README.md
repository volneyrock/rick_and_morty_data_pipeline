# Rick and Morty Flow

Este projeto utiliza Prefect para criar um fluxo que busca personagens do Rick and Morty e suas localizações, e salva os dados em um arquivo JSON.

O projeto é gerenciado com `poetry` para dependências e `pre-commit` para garantir a qualidade do código.

## Requisitos

- Python 3.8+
- Poetry
- pre-commit

## Instalação

### Clonar o repositório

```bash
git clone git@github.com:volneyrock/rick_and_morty_data_pipeline.git
cd rick-and-morty-flow
```

### Configurar o ambiente virtual

Use o poetry para instalar as dependências e configurar o ambiente virtual:

```bash
poetry install
```

### Ativar o ambiente virtual

```bash
poetry shell
```

### pre-commit
Este projeto utiliza `pre-commit` para manter a qualidade do código. Certifique-se de instalar os hooks após clonar o repositório:

```bash
pre-commit install
```

### Para executar o fluxo

```bash
python flows.py
```

Após a execução, um arquivo `rick_and_morty.json` será gerado contendo os dados dos personagens e suas localizações.

## Para executar os testes

```bash
pytest
```

### Estrutura do projeto

```
.
├── api                      # Módulo para interagir com a API
│   ├── __init__.py
│   ├── api.py
├── tasks                    # Módulo com as tarefas Prefect
|   ├── __init__.py
│   ├── prefect_tasks.py
├── tests                    # Módulo com os testes
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_tasks.py
├── .gitignore
├── .pre-commit-config.yaml  # Configuração do pre-commit
├── flows.py                 # Arquivo principal do fluxo Prefect
└── poetry.lock
├── pyproject.toml           # Configuração do poetry
├── README.md
```
