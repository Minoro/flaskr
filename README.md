# flaskr
Tutorial do Flask

Esse repositório contém os códigos disponibilizados no [tutorial oficial do Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/).

A Aplicação consiste em um site para postagem de texto. Usuários autenticados podem criar e ler posts além de poderem editar e excluir as próprias postagens.

Para rodar o servidor de desenvolvimento utilize os comandos:

```
export FLASK_APP=flaskr
export FLASK_ENV=development

flask run
```
**Atenção**: não rodar os comandos em produçao.

Para testar o código do respositório utilizar o comando:
```
pytest
```
