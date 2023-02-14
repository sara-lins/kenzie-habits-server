# Kenzie Habits Server

## Descrição do projeto (Project description)

Servidor elaborado para aplicação To-do list, com CRUD de tasks ligado ao Database Postgres.

Server designed for To-do list application, with tasks CRUD linked to Database Postgres.

Tecnologias (technologies): Python, Django REST Framework, UUID, PostgreSQL.

Endpoint API:

Documentation:

## Iniciando o projeto localmente

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

3. Instale os pacotes:

```shell
pip install -r requirements.txt
```

4. Agora é só rodar os testes no diretório principal do projeto:

```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:

```shell
pytest --testdox
```
