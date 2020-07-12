import os

from flask import Flask

from sqlalchemy import exc
from sqlalchemy.orm import exc as e

from students.blueprints import restapi
from students.ext import database
from students.ext.database import db
from students.models import Aluno

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "studentdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
database.init_app(app)
restapi.init_app(app)


@app.cli.command()
def create_db():
    """Creates database"""
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
    app.cli.add_command(app.cli.command()(create_db))
