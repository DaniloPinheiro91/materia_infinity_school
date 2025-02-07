# cria uma lista com varios elementos duplicados
elementos = ['maça', 'amigo', 'elefante', 'maracuja', 'elefante', 'pessoas', 'pessoas', 'maça',
            'amigo','inteligencia', 'amigo', 'macaco', 'macaco', 'macaco', 'macaco']

print(f'A lista de elementos é: {elementos}\n')
# Retira a duplicidade criando uma nova lista para mostrar os elementos e tirar a quantidade
tirando_duplicidade = list(set(elementos))
print(f'Tirando as Duplicidades para contar a quantidade: {tirando_duplicidade}\n')
# pescorre a lista tirando_duplicidade e imprime a quantidade de cada intem da primeira lista
for item in tirando_duplicidade:
    quantidade = elementos.count(item)
    print(f'{item}: {quantidade}\n')
