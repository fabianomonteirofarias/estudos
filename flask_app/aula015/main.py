# AULA 015 - REST API - Part 1

from flask import Flask, render_template, Response, request, redirect, url_for
from models import db, Estudante
import json

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///estudantes.db"


@app.route("/")
def index():
    # estudantes = Estudante.query.all()
    # result = [e.to_dict() for e in estudantes]
    rows = db.session.execute("select * from estudante").fetchall()
    result = [dict(row) for row in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route("/view/<int:id>", methods=["GET"])
def view(id):
    row = db.session.execute("select * from estudante where id %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@app.route("/add", methods=["POST"])
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return app.response_class(response=json.dumps({"status": "success", "data":estudante.to_dict()}), status=200, content_type="application/json")


@app.route("/delete/<int:id>", methods=["GET", "DELETE"])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form["nome"]
    estudante.idade = request.form["idade"]
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


if __name__ == "__main__":
    db.init_app(app=app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
