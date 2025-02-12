produtos = {}

for i in range(5):
    nome_produto = input(f"Digite o nome do produto {i + 1}: ")
    preco_produto = float(input(f"Digite o preço do produto {nome_produto}: R$ "))
    produtos[nome_produto] = preco_produto
valor_total = sum(produtos.values())

print('-='*30)
print("\nResumo da compra:")

for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {valor_total:.2f}")
