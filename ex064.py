valor = cont = soma = 0
print('Para finalizar digite [999]')
valor = int(input('Digite um número: '))
while valor != 999:
    cont += 1
    soma += valor
    valor = int(input('Digite um número: '))
print(f'A quantidade de número usados foi {cont} e a soma entre eles é {soma}')
