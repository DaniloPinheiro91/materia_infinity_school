valor = float(input('Insira o valor do produto para gerar o desconto:'))

desconto = 5/100 * valor
valor_desconto = valor - desconto

print (f'O valor concebido em desconto é de {desconto}')
print(f'O desconto no produto foi de 5% você vai pagar:  {valor_desconto}')
