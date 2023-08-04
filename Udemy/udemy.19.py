try:
    valor = int(input('Digite um valor: '))
    print(valor)
except ValueError:
    print(('Favor digitar um valor em numeros'))
finally:
    print('codigo ok')
'''else:
    print('voce acertou')
    resultado  =  valor*9
    print(resultado)'''
