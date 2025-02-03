numero = int(input('Insira um numero para desconrir a taboada: '))

for i in range(11):
    taboada = numero * i
    print(f'{i} X {numero} = {taboada}')
