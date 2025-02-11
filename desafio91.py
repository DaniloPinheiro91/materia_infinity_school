import random
jogadores = []

for i in range(4):
    i+= 1
    jogador = {}
    num = random.randint(1, 6)
    jogador['jogador'] = i
    jogador['numero_sorteado'] = num
    print(jogador)
    jogadores.append(jogador)
jogadores_ordenado = sorted(jogadores, key=lambda x: x['numero_sorteado'], reverse=True)
print('-'*30)
print('Ranking dos Jogadores: ')
print('-'*30)
for i in jogadores_ordenado:
    print(f'{i}')

