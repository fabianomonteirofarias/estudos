# AULA 002 - CRIANDO ROTAS E CONFIGURAÇÕES

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


@app.route("/page")
def page_one():
    return "Page"


if __name__ == "__main__":
    app.run()
