numero = 20
impar = 0
par = 0
for numero in range (1, 20):
    print(f'Verificando os numeros: {numero}')
    if numero % 2 == 0:
        par += 1
    elif numero == 15:
        break
    else:
        impar += 1

print ('Ao localizar o numero 15 o laço foi interrompido...')
print(f'No intervalo de "0 a 20" existe {par} numeros pares e {impar} numeros impares')
