import random

def lancar_dados():
    dado1 = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6
    dado2 = random.randint(1, 6)  # Gera outro número aleatório entre 1 e 6
    print(f'Os numeros gerados é {dado1} e {dado2}')
    print('-=-'*20)
    return dado1 + dado2  # Retorna a soma dos dois dados

resultado = lancar_dados()
print(f"Resultado do lançamento: {resultado}")