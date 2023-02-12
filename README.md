# Kenzie Habits Server

## Descrição do projeto (Project description)

Servidor elaborado para aplicação To-do list, com CRUD de tasks ligado ao Database Postgres.

Server designed for To-do list application, with tasks CRUD linked to Database Postgres.

Tecnologias (technologies): Python, Django REST Framework, UUID, PostgreSQL.

Endpoint API:

Documentation:

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:

```shell
pip install pytest-testdox pytest-django
```

4. Agora é só rodar os testes no diretório principal do projeto:

```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:

```shell
pytest --testdox
```
