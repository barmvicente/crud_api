import os

from datetime import datetime

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import exc
from sqlalchemy.orm import exc as e

from modules.response import response


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "studentdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Aluno(db.Model):
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    ano_escolar = db.Column(db.Integer, nullable=False)
    turma = db.Column(db.String(80), nullable=False)
    responsavel = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    nascimento = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Nome: {self.nome}>"


@app.route("/", methods=["GET", "POST"])
def home():
    alunos = Aluno.query.all()
    return response(alunos)

@app.route("/insert", methods=["POST"])
def insert():
    if request.json:
        nasc = request.json.get("nascimento")
        nascimento = datetime.strptime(nasc, '%d/%m/%Y')
        aluno = Aluno(
            nome=request.json.get("nome"),
            ano_escolar=request.json.get("ano_escolar"),
            turma=request.json.get("turma"),
            responsavel=request.json.get("responsavel"),
            telefone=request.json.get("telefone"),
            nascimento=nascimento,
        )
        try:
            db.session.add(aluno)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
    alunos = Aluno.query.all()
    return response(alunos)

@app.route("/update", methods=["POST"])
def update():
    newnome = request.json.get("newnome")
    oldnome = request.json.get("nome")
    aluno = Aluno.query.filter_by(nome=oldnome).first()

    if not aluno:
        return jsonify('Aluno não existente!')
    
    if newnome:
        aluno.nome = newnome

    newano = request.json.get("newano")
    if newano:
        aluno.ano_escolar = newano

    newturma = request.json.get("newturma")
    if newturma:
        aluno.turma = newturma

    newresponsavel = request.json.get("newresponsavel")
    if newresponsavel:
        aluno.responsavel = newresponsavel

    newtelefone = request.json.get("newtelefone")
    if newtelefone:    
        aluno.telefone = newtelefone

    newnascimento = request.json.get("newnascimento")
    if newnascimento:
        aluno.nascimento = newnascimento

    db.session.commit()
    return response([aluno])

@app.route("/delete", methods=["POST"])
def delete():
    cod = request.json.get("cod")
    aluno = Aluno.query.filter_by(id=cod).first()
    try:
        db.session.delete(aluno)
        db.session.commit()
    except e.UnmappedInstanceError:
        db.session.rollback()
        return jsonify("Aluno não existente!")
    return response([aluno])

@app.route("/filter", methods=["POST"])
def filter():
    alunos = Aluno.query
    nome = request.json.get("nome")
    ano = request.json.get("ano_escolar")
    turma = request.json.get("turma")
    if nome:
        alunos = alunos.filter_by(nome=nome)
    if ano:
        alunos = alunos.filter_by(ano_escolar=ano)
    if turma:
        alunos = alunos.filter_by(turma=turma)
    
    alunos = alunos.all()
    return response(alunos)
  

if __name__ == "__main__":
    app.run(debug=True)
