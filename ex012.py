produto = float(input('Digite o valor do produto:'))
desconto = produto*5/100
final = produto-desconto
# novo = produto - (produto*5/100)
print('O valor do produto com 5% de desconto é: {:.2f}'.format(final))