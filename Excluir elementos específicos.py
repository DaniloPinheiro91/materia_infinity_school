numeros = [5, 4, 9, 4, -1, 18, -7, -5, 7, 19, -43, 55, 11, -14]

for i in range(len(numeros)-1, -1, -1):
    if numeros[i] < 0:
        numeros.remove(numeros[i])

print(numeros)
