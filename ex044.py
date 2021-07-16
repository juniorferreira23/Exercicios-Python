p = float(input('Digite o preço do produto: '))
print(''' {}FORMAS DE PAGAMENTO:
[1] - à vista dinheiro/cheque: 10% de desconto
[2] - à vista no cartão: 5% de desconto
[3] - em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros{}'''.format('\033[33m','\033[m'))
f = int(input('Digite entre 1 e 4 a forma de pagamento: '))
if f == 1:
    print('O valor do seu produto com 10% de desconto é R$:{:.2f}'.format(p - (p*10/100)))
elif f == 2:
    print('O valor do seu produto com 5% de desconto é R$:{:.2f}'.format(p - (p*5/100)))
elif f == 3:
    print('O valor do seu produto parcelado é 2x de R$:{:.2f}'.format(p/2,p))
elif f == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('O valor do seu produto parcelado em {}x com 20% de juros é R$:{:.2f}'.format(parcelas,(p + (p*20/100))/parcelas))
else:
    print('Opção inválida, tente novamente.')