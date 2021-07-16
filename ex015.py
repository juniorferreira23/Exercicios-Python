dia = int(input('Digite a quantidade de dias de aluguel do carro:'))
km = float(input('Digite a quantidade de Km percorridos:'))
pago = (dia*60)+(km*0.15)
print('O valor a ser pago é de: R${}'.format(pago))
