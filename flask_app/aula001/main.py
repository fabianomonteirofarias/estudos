# AULA 001 - Instalando Flask

from flask import Flask

app = Flask(__name__)


@app.route("/")
def first_page():
    return "Hello, world!"


def teste():
    return "TESTANDO 1"


def teste2():
    return "TESTANDO 2"


app.add_url_rule("/teste", "teste", teste)
app.add_url_rule("/teste-2", "teste-2", teste2)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
