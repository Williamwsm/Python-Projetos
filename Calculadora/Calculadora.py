while True:
    num1 = input('Digite um numero:')
    operador = input('escolha uma operacao "+ - * /"')
    num2 = input('Digite mais um numero: ')


    try:
        numValidos = None
        num1Float = float(num1)
        num2Float = float(num2)
        numValidos = True
    except:
        numValidos = None
    if numValidos is None:
        print('Um dos numeros digitado estar invalido')
        continue

    operadoresPermitidos  = '+-/*'

    if operador not in operadoresPermitidos:
        print('O operador digitado é invalido')
        continue
    if len(operador)>1:
        print('Digite apenas um operador')
        continue
    print('Realizando a sua conta. O resultado aparecerar abaixo:')
    if operador == '+':
        print(f'{num1Float} + {num2Float} =', num1Float + num2Float )
    elif operador == '-':
        print(f'{num1Float} - {num2Float} =', num1Float - num2Float )

    elif operador == '/':
        print(f'{num1Float} / {num2Float} =', num1Float / num2Float )
    elif operador == '*':
        print(f'{num1Float} * {num2Float} =', num1Float * num2Float )
    else:
        print('Nunca deveria chegar aqui')
        sair = input('Quer sair? [s]im:').lower().startswith('s')
        if sair is True:
            break

