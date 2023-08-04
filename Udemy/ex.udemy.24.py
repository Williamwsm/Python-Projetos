funcionarios = ['ana','marcos','alice','predo','sophia','bruno','melissa']
turnoDia = ['ana','marcos','alice','melissa']
turnoNoite = ['predo','sophia','bruno']
temCarro = ['marcos','alice','bruno','melissa']
diaCarro = set(turnoDia).intersection(temCarro)
noiteCarro = set(turnoNoite).intersection(temCarro)
nCarro = set(funcionarios).difference(temCarro)
print(f'nao tem carro {nCarro}')
print(f'tem carro e trabalha pelo dia{diaCarro}')
print(f'tem carro e trabalha pela noite{noiteCarro}')

'''for x in funcionarios:
    if x in temCarro and x in turnoDia:
        diaCarro.append(x)

    if x in temCarro and x in turnoNoite:
        noiteCarro.append(x)

    if not x in temCarro:
        nCarro.append(x)

'''