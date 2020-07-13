# crud_api

## requisitos
> python3
pip3

## instalar requeriments
`pip install requeriments.txt`

## rodar app
`python -m students.app`

## criar base de dados
> abrir o shell do Python
```python
from studentesmanager import db
db.create_all()
```

## funcionamento

### localhost/ - listagem de alunos

### localhost/insert - inserção de aluno
O seguinte payload deve ser recebido:
```json
{
    "nome": "String",
    "ano_escolar": "Integer",
    "turma": "String",
    "responsavel": "String",
    "telefone": "String - formato DDDnumero",
    "nascimento": "DateTime - formato dd/mm/YYYY"
}
```

retorno: lista de alunos com novo aluno inserido

### localhost/update - atualização de dados de aluno
O seguinte payload deve ser recebido:
```json
{
    "nome": "String",
    "newnome": "String (opcional)",
    "newano_escolar": "Integer (opcional)",
    "newturma": "String (opcional)",
    "newresponsavel": "String (opcional)",
    "newtelefone": "String - formato DDDnumero (opcional)",
    "newnascimento": "DateTime - formato dd/mm/YYYY (opcional)"
}
```

retorno: aluno atualizado

### localhost/delete -deleção de aluno
O seguinte payload deve ser recebido:
```json
{
    "cod": "Integer - id do aluno"
}
```

retorno: aluno deletado

### localhost/filter - filtro de aluno
O seguinte payload deve ser recebido:
```json
{
    "nome": "String (opcional)",
    "ano_escolar": "Integer (opcional)",
    "turma": "String (opcional)",
    "responsavel": "String (opcional)",
    "telefone": "String - formato DDDnumero (opcional)",
    "nascimento": "DateTime - formato dd/mm/YYYY (opcional)"
}
```

retorno: alunos que correspondem aos parâmetros informados
