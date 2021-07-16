cont = soma = 0
print('Digite [999] para parar')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A quantidade de números digitados foi {cont} e a soma entre eles é {soma}')
