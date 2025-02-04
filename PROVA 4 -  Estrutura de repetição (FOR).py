inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
soma_pares = 0
encontrou_pares = False

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma_pares += num
        encontrou_pares = True

if encontrou_pares:
    print(f"A soma dos números pares no intervalo é: {soma_pares}")
else:
    print("Não há números pares no intervalo.")
