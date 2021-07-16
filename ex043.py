p = float(input('Digite seu peso:'))
a = float(input('Digite a sua altura:'))
imc = p / (a**2)
if imc < 18.5:
    print('Você está abaixo do peso normal! :(')
elif imc < 25:
    print('Você está com o peso ideal! ;)')
elif imc < 30:
    print('Você está com sobrepeso! :(')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida')
