valores = []
quantidade = 10
par = 0
impar = 0
for lista in range(quantidade):
    valor = int(input(f'Digite o valor - {lista + 1}: '))
    valores.append(valor)
    if valor == 0:
        break
    if valor % 2 == 0:
        par += 1
        print(f'{valor} é par')
    else:
        impar += 1
        print(f'{valor} é impar')


print (f'Lista de valores: {valores}')
print (f'Existe {par} numero(s) par(es) na lista')
print (f'Existe {impar} numero(s) impar(es) na lista')
