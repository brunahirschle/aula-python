
produto = {}
soma = 0

for i in range(5):
    nome = input('Digite o nome do produto:')
    preco = float(input('Digite o preço: '))
    produto[nome] = preco
    soma += preco
    print(produto)

print(f'o valor total da compra foi R${soma}')