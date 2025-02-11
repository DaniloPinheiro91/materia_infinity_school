alunos = []

for i in range(0, 3):
    aluno = {}
    aluno['nome'] = input('Nome do aluno: ')

    n1 = [] # armazena as notas dos alunos
    for n in range(0, 4):
        nota = float(input(f'Insira a nota {n+1} do aluno:'))
        n1.append(nota)

    media = sum(n1)/4 # calcula a media
    aluno['media'] = media

    if media >=5.0:
        aluno['situacao'] = 'Aprovado'
    else:
        aluno['situacao'] = 'Reprovado'

    alunos.append(aluno)#adiciona o dicionario a lista
print('-'*30)
for aluno in alunos:
    for chave, valor in aluno.items():
        print(f'{chave}: {valor}')
    print('-'*30)

