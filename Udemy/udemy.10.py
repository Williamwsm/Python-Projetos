'''Set (Listas)
    simula a listas
    evita itens duplicados
    nao utilioza index'''


lista1 = [10,20,30,40,50]
lista2 = [10,20,60,70]
num1 = set(lista1)
num2 = set(lista2)
#uniao  de todos os  elementos sem repetilos  Union
print(num1 | num2)
num3 = num1.union(num2)
#remove os elementos em comum do num1    Difference
print(num1 - num2)
num3 = num1.difference(num2)
# retira os duplicados nas duas listas     Symmetric Difference
print(num1 ^num2)
num3 = num1.symmetric_difference(num2)
# o que é dupliacado em ambas as listas     And
print(num1 & num2)
