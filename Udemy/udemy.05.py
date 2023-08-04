
corCliente =str(input('Informe a cor que voce deseja: ')).lower()
if corCliente in cores:
    print(f'A cor {corCliente} esta em nosso estoque')
else:
    print(f'Nao temos a cor {corCliente} em nosso estoque')