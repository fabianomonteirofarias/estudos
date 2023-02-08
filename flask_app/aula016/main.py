# AULA 016 - REST API - Part 2

from flask import Flask
from aula016.models.models import db
from aula016.controllers.estudante import app as estudante_controller
from aula016.controllers.disciplina import app as disciplina_controller

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///estudantes.db"

app.register_blueprint(estudante_controller, url_prefix="/estudante/")
app.register_blueprint(disciplina_controller, url_prefix="/disciplina/")

if __name__ == "__main__":
    db.init_app(app=app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
