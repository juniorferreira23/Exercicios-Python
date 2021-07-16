#MINHA 2º VERSÃO
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = stc= 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite o valor da matriz [{l}, {c}]: '))
        if lista[l][c] % 2 == 0:
            somapar += lista[l][c]
        if c == 2:
            stc += lista[l][c]
print('-=-' * 11)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]', end='')
    print('')
print('-=-' * 11)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {stc}')
print(f'O maior valor da segunda linha é {max(lista[1])}')

#MINHA 1º VERSÃO
'''lista = [[], [], []]
somapar = sc3 = 0
for c in range(0,3):
    n1 = int(input(f'Valor para [0, {c}]: '))
    lista[0].append(n1)
for c in range(0,3):
    n2 = int(input(f'Valor para [1, {c}]: '))
    lista[1].append(n2)
for c in range(0,3):
    n3 = int(input(f'Valor para [0, {c}]: '))
    lista[2].append(n3)
print('-=-'*7)
for c in range(0,len(lista[0])):
    print(f'[{lista[0][c]:^5}]', end='')
    if lista[0][c] % 2 == 0:
        somapar += lista[0][c]
    if c == 2:
        sc3 += lista[0][c]
print('')
for c in range(0,len(lista[1])):
    print(f'[{lista[1][c]:^5}]', end='')
    if lista[1][c] % 2 == 0:
        somapar += lista[1][c]
    if c == 2:
        sc3 += lista[1][c]
print('')
for c in range(0,len(lista[2])):
    print(f'[{lista[2][c]:^5}]', end='')
    if lista[2][c] % 2 == 0:
        somapar += lista[2][c]
    if c == 2:
        sc3 += lista[2][c]
print('\n', '-=-'*7)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {sc3}')
print(f'O maior valor da segunda linha é {max(lista[1])}')'''