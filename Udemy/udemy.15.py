''' List comprehension
        mais simples de se escrever
        utilizado quando voce precisa criar uma nova lista a partir de uma existente
        [expressao for in itens]
'''

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
#frutas2  =[]

'''for x in frutas1:
    if 'b' in x:
        frutas2.append(x)
print(frutas2)'''

frutas2 = [x for x in frutas1 if 'm' in x]
print(frutas2)
