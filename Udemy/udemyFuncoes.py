def somar():
    print('Essa funcao vai somar dois valores')

def multi():
    print('Essa funcao vai multiplicar dois valores')

def findIndex(toFind,intem):
    for i , v in enumerate(toFind):
        if v == intem:
            return i
    return -1