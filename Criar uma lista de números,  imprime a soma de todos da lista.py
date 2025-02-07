import random
#Cria uma lista com 10 numeros inteiros aleatorios usando RANDOM
numero = []
for i in range(10):
    i=random.randint(1,100)
    numero.append(i)
print(f'A lista aleatoria criada é: {numero}')
soma_total = 0
for soma in numero:
    soma_total = sum(numero)

print(soma_total)

