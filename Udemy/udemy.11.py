aluno = {'nome': 'Ana', 'idade': 18, 'notaFinal': 'A', 'Aprovada': True}
aluno["nome"] = 'ricardao'
aluno.update({'nome': 'jose','notaFinal': 'B',})
aluno.update({'endereco': 'rua C'})
del aluno ['idade']

print(aluno.get('endereco', 'nao existe'))
for k , v  in aluno.items():
    print(f'{k} recebe {v}')