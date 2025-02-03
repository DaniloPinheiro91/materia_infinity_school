# Jogo da adivinhação
numero_escolhido = 0
tentativas = 0
numero_sorte = 7

print ('Vamos jogar um jogo de adivinhação?')
print ('tente acertar um numero de 0 a 20')
while numero_escolhido != numero_sorte:
    numero_escolhido = int(input('tentativa: '))

    tentativas += 1

    if numero_escolhido == numero_sorte:
        print(f'Parabéns! Você acertou o número da sorte em {tentativas} tentativas.')
    else:
        if tentativas >= 3:
            print('Você esgotou todas as suas tentativas, vamos jogar novamente! dessa vez você consegue acertar')
            tentativas = 0
            numero_escolhido = 0
        else:
            print('Não foi dessa vez, tente novamente...')
