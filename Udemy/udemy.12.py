'''Lambda
    uma funçao pequena e sem nome
    muito utilizada dentro de outras funcoes
    codigo mais "clean"'''

def somar(x):
    func2 = lambda x: x +10
    return func2(x) *4
print(somar(2))

somar10 = lambda x, y: x+y +10
print(somar10(2,6))

