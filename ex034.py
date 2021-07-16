s = float(input('Digite o valor do seu salário R$:'))
if s > 1250:
    print('O seu salário com aumento é R${}'.format(s + s*10/100))
else:
    print('O seu salário com aumento é R${}'.format(s + s*15/100))
