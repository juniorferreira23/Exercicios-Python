viagem = float(input('Digite a distancia em Km da sua viagem:'))
print('Você esta prestes a começar uma viagem de {:.2f}Km.'.format(viagem))
#preço = viagem * 0.50 if <= 200 else viagem * 0.45
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('O custo da sua viagem é de R${:.2f}'.format(preço))
