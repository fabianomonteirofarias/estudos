# AULA 004 - Construção de URL

from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "Alá, um desempregado."


@app.route("/admin")
def admim():
    return "Adm tá on."


@app.route("/guest/")
@app.route("/guest/<name>")
def guest(name=""):
    if name == "":
        return "Desempregado detectado."
    else:
        return f"Desempregado detectado. Nome: {name}"


@app.route("/user/")
@app.route("/user/<name>")
def user(name=""):
    if name == "admin":
        return redirect(url_for("admim"))
    else:
        return redirect(url_for("guest", name=name))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
