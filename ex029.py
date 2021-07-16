v = int(input('Qual a velocidade atual do seu carro?'))
multa = (v - 80) * 7
if v > 80:
    print('Você foi multado! Exceu o limite permitido de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
