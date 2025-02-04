num_alunos = int(input("Digite o número de alunos: "))
soma_medias = 0

for quantidade in range(num_alunos):

    nome = input(f"\nDigite o nome do {quantidade+1}º aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"\nAluno: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

    soma_medias += media

media_geral = soma_medias / num_alunos

print(f"\nMédia geral da turma: {media_geral:.2f}")
