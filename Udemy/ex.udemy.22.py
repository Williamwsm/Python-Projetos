carneTemperatura = float(input('informe a temperatura da carne: '))
if carneTemperatura < 48:
    print('Por favor cozinhe por mais uns minutos')
elif carneTemperatura >= 48 and carneTemperatura < 54:
    print("Selada")
elif carneTemperatura >= 54 and carneTemperatura < 60:
    print('Ao ponto para o mal')
elif carneTemperatura >= 60 and carneTemperatura < 65:
    print('Ao ponto')
elif carneTemperatura >= 65 and carneTemperatura < 71:
    print('Ao ponto para o bem')
else:
    print('Bem passada')