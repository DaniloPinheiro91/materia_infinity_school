nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input ('Insira a segunda nota: '))
media = float((nota1 + nota2)/2)

if nota1 >= 6 and nota2 >= 6:
    print (f'Suas notas são {nota1} e {nota2}, sua media é {media}. Você está aprovado')
elif nota1 < 6 and nota2 < 6:
    print (f'Suas notas são {nota1} e {nota2}, sua media é {media}. Você está de recuperação. ')
elif media >= 6:
    print (f'Suas notas são {nota1} e {nota2}, sua media é {media}. Você tirou uma nota vermelha porém, está aprovado.')
elif media < 6:
    print (f'Suas notas são {nota1} e {nota2}, sua media é {media}. Você está de recuperação.')
else:
    print('Opção invalida')


