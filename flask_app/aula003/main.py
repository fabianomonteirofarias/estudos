# AULA 003 - Criando URL dinâmicas

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
def index(name = "No Register Member"):
    return f"Welcome, {name}"


@app.route("/blob/")
@app.route("/blob/<int:postID>")
def blob(postID = 0):
    if postID > 0:
        return f"Bro: {postID}"
    else:
        return "Already, have a job?"


if __name__ == "__main__":
    app.run(debug=True, port=3000)
