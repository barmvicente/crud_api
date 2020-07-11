from flask import jsonify

def response(alunos):
    response = []
    for a in alunos:
        aluno = {
            'nome': a.nome,
            'nascimento': a.nascimento,
            'ano': a.ano_escolar,
            'turma': a.turma,
            'responsavel': a.responsavel,
            'telefone': a.telefone,
            'cod_aluno': a.id
        }
        response.append(aluno)
    return jsonify(response)