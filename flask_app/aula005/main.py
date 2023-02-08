# AULA 005 - WEB arquivos estáticos

from flask import Flask

app = Flask(__name__, static_folder="static")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
