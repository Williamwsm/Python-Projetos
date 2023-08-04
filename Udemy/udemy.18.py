''' erros
        bons para testes
        nao realiza o 'stop' no programa
        mensagens customizadas quando encontrar um erro

'''
#quando tiver um erro ele nao vai parar o codigo no erro e vai ennviar uma mensagem sobre
try:
    letras = ['a','b','c']
    print(letras[3])
except IndexError:
    print('erro no indece')
