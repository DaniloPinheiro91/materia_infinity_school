contato = {}

contato['nome'] = str(input('Qual o nome do contato?'))
contato['telefone'] = int(input('Qual o telefone para contato ( apenas numeros)'))
contato['email'] = str(input('Qual o email para contato?'))

print('Imprimindo as informações do contato:\n')
for chave, valor in contato.items():
    print (f'{chave.capitalize()}: {valor}')
