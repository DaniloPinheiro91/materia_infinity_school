idade = int(input('Qual a sua idade ?'))
cnh = input('Você possui habilitação? escolha entre "sim" e "nao"')
sim = 'sim'
nao = 'nao'

if cnh in sim and idade >=18:
    print ('Parabens, você é maior de idade e possui habilitação para dirigir')
elif cnh in nao and idade >=18:
    print ('Você é maior de idade porém, não é habilitado')
elif cnh in sim and idade <18:
    print ('Você não pode ser habilitado, você é menor de idade')
elif idade < 18:
    print('Você é menor de idade')
else:
    print ('Opção invalida')

