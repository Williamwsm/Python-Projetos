peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura em centimetros: '))
imc = peso/((altura/100)**2)
if imc < 18.5:
    print('magreza')
elif imc >= 18.5  and imc <= 24.9:
    print('normal')
elif imc >=25 and imc <= 29.9:
    print('sobrepeso')
elif imc >= 30 and imc <=39.9:
    print('Obsidade')
else:
    print('Obsidade grave')