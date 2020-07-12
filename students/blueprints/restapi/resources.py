from datetime import datetime

from flask import abort, jsonify, request
from flask_restful import Resource

from sqlalchemy import exc
from sqlalchemy.orm import exc as e

from students.models import Aluno
from students.ext.database import db
from students.modules.response import response

class StudentResource(Resource):
    def get(self):
        alunos = Aluno.query.all() or abort(204)
        return jsonify(
            {"alunos": response(alunos)}
        )


class StudentInsertResource(Resource):
    def post(self):
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
        return jsonify(
            {
                "aluno": response(alunos),
                "ação": "inserido",
            }
        )

class StudentUpdateResource(Resource):
    def post(self):
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

        return jsonify(
            {
                "aluno": response(aluno),
                "ação": "atualizado",
            }
        )

class StudentDeleteResource(Resource):
    def post(self):
        cod = request.json.get("cod")
        aluno = Aluno.query.filter_by(id=cod).first()
        try:
            db.session.delete(aluno)
            db.session.commit()
        except e.UnmappedInstanceError:
            db.session.rollback()
            return jsonify("Aluno não existente!")
        return jsonify(
            {
                "aluno": response(aluno),
                "ação": "deletado",
            }
        )

class StudentFilterResource(Resource):
    def post(self):
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
        
        return jsonify(
            {"alunos": response(alunos)}
        )
        