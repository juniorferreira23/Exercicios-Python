#SEGUNDA VERSÃO MAIS OTIMIZADA COM DOIS FOR E JÁ COLOCANDO VARIAVEIS DENTRO DA LISTA
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite o valor da matriz [{l}, {c}]: '))
print('-=-' * 20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]', end='')
    print('')

#MINHA 1º VERSÃO ^^
'''lista = [[], [], []]
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
for c in lista[0]:
    print(f'[ {c} ]', end='')
print('')
for c in lista[1]:
    print(f'[ {c} ]', end='')
print('')
for c in lista[2]:
    print(f'[ {c} ]', end='')'''