# AULA 006 - Métodos HTTP

from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder="public")


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        return "POST " + str(dumps(request.form))
    return "GET"


if __name__ == "__main__":
    app.run(debug=True, port=3000)