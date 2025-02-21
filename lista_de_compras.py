def criar_lista_de_compras(*lista):
    contador = 0
    print('=-=' * 30)
    for i in lista:
        contador += 1

        print(f'Item {contador} da lista: {i}')
    print('=-=' * 30)   

lista_compra = []
item = 'lista'
while item != 'sair':
    item = input('Insira o nome do item para lista de compra:\n ou digite ( sair) para sair: ')

    lista_compra.append(item)
lista_compra.pop()

criar_lista_de_compras(*lista_compra)