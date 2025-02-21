# exporta a biblioteca functools
from functools import reduce

#Cria uma função que compara uma lista de strings
def recebe_palavras(*lista):
    # usa lambda para criar uma mini função de comaprçao
    #le o item X e Y com len() e compara os 2 com if e else 
    resultado = reduce(lambda x, y: x if len(x) > len(y) else y, lista)
    #retirna a variavel resultado dessa comparação apos percorer tora a lista com reduce
    return print (f'A Maior String da lista é: {resultado}')

# cria uma lista de palavras vazias para o input do usuario
lista_palavras = []

# faz um laço for com range 5 para gerar 5 palavras com o input do usuario
for i in range (5):
    # a variavel palavra receve o input do usuario
    palavra = input('Insira uma palavra: ')
    # a variavel lista_palavras armazena os inputs do usuario da variavel palavra
    lista_palavras.append(palavra)

# chama a função criada e usa o *args para recebber varios parametros
recebe_palavras(*lista_palavras)