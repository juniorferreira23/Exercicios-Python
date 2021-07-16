#2º VERSÃO REFEITA COM OUTRA TECNICA DE SABER O MAIOR E O MENOR USANDO LEN
# E PODENDO DA APPEND DIRETO NO INPUT
lista = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(input('Nome: ').strip().title())
    pessoa.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    op = ' '
    while op not in 'SN':
        op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break
print('-=-'*20)
print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if maior in p:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ',end='')
for p in lista:
    if menor in p:
        print(f'[{p[0]}]', end=' ')

#MINHA 1º VERSÃO  USANDO CONTADOR
'''lista = []
pessoa = []
maior = menor = cont = 0
while True:
    n = input('Nome: ').strip().title()
    p = float(input('Peso: '))
    if cont == 0:
        maior = menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
    cont += 1
    pessoa.append(n)
    pessoa.append(p)
    lista.append(pessoa[:])
    pessoa.clear()
    op = ' '
    while op not in 'SN':
        op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break
print('-=-'*20)
print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if maior in p:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ',end='')
for p in lista:
    if menor in p:
        print(f'[{p[0]}]', end=' ')'''
