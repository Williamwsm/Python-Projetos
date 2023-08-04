''' Filter funcion
        muito usada em listas
        aplicar uma funcao a um Iterable, filtrando os items. (list, tuple,dic)
'''


valores = [10,12,34,44,57]


def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores )))