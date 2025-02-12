import datetime
cadastro = {}
cadastro['nome'] = input('Insira o nome: ')
cadastro['nascimento'] = int(input('Ano de nascimento: '))
cadastro['sexo'] = input('qual seu sexo? digite "M" para Masculino e "F" para feminino: ')
cadastro['carteira_de_trabalho'] = int(input('Numero da Carteira de Trabalho (caso não possua digite "0"): '))
cadastro['idade'] = datetime.datetime.now().year - cadastro['nascimento']
verifica_carteira = cadastro['carteira_de_trabalho']
if verifica_carteira != 0:
    cadastro['ano_de_contratacao'] = int(input('Qual o ano de contratação? '))
    cadastro['salario'] = float(input('Qual o Salario mensal? '))
    idade_atual = datetime.datetime.now().year - cadastro['nascimento']
    contribuicao = datetime.datetime.now().year - cadastro['ano_de_contratacao']
    if cadastro['sexo'] == 'F' and idade_atual < 62 and contribuicao < 15:
        cadastro['ano_aposentadoria'] = (62 - idade_atual) + datetime.datetime.now().year
    elif cadastro['sexo'] == 'M' and idade_atual < 65 and contribuicao < 20:
        cadastro['ano_aposentadoria'] = (65 - idade_atual) + datetime.datetime.now().year
    else:
        cadastro['ano_aposentadoria'] = 'Você já pode aposentar!'
print('-='*30)
for chave, valor in cadastro.items():
    print (f'{chave}:{valor}')
