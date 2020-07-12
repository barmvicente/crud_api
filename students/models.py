from students.ext.database import db

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