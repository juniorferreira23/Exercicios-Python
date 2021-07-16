cont = soma = maior = menor = 0
c = 'S'
while c == 'S':
    num = int(input('Digite um número: '))
    c = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
média = soma / cont
print(f'Você digitou {cont} números, a média dos números é {média:.2f}, o maior número é {maior} e o menor é {menor}')
