from datetime import date
totalmenor = 0
totalmaior = 0
anoatual = date.today().year
for pessoas in range(1,8):
    nasc = int(input(f'Em que ano a {pessoas}º pessoa nasceu? '))
    idade = anoatual - nasc
    if idade < 20:
        totalmenor += 1
    elif idade >= 20:
        totalmaior += 1
print('-=-'*4)
print('|RESULTADO|')
print('-=-'*4)
print(f'A quantidade de menores de 20 anos é: {totalmenor}')
print(f'E a quantidade de maiores de idade é: {totalmaior}')
