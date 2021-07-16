lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para posição {cont}: ')))
maior = max(lista)
menor = min(lista)
print(f'O maior valor foi {maior} na posição: ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor foi {menor} na posição: ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')

# Versão Guanabará
'''lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}º: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor foi: [{maior}] ele apareceu na posição: ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor foi: [{menor}] ele apareceu na posição: ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')'''
