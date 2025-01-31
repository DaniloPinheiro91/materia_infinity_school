numero = int(input('Escolha um numero para o calculo fatorial: '))

if numero < 0:
    print('O numero informado é negativo, não é possivel efetuar o calculo')
else:
    fatorial = 1

calculo = 1
while calculo <= numero:
    fatorial *= calculo
    calculo += 1
print (f'O fatorial de {numero} é {fatorial}.')
