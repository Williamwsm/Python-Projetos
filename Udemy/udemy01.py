def soma(*num):
    soma = 0
    for x in num:
        soma += x
    return soma

x = soma(1,5,8,4,3)
print(x)