#2º VERSÃO DEPOIS DE VER A RESOLUÇÃO
lista = []
while True:
    nome = input('Nome: ').strip().title()
    while True:
        n1 = float(input('Primeira nota: '))
        if 0 <= n1 <= 10:
            break
    while True:
        n2 = float(input('Segunda nota: '))
        if 0 <= n2 <= 10:
            break
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar?  [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break
print(f'{"No.":<8}{"NOME":^8}{"MÉDIA":>8}')
print('-'*25)
for p , n in enumerate(lista):
    print(f'{p:<8}{n[0]:^8}{n[2]:>8.1f}')
while True:
    opc = int(input('[999] para interroper. Mostra nota do aluno: '))
    if opc == 999:
        print('PROGRAMA FINALIZADO...')
        break
    elif opc < len(lista):
        print(f'As notas de {lista[opc][0]} são {lista[opc][1]}')

#1º VERSÃO
'''lista = []
nome = []
notas = []
while True:
    nome.append(input('Nome: ').strip().title())
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    media = (n1 + n2) / 2
    notas.append(media)
    nome.append(notas[:])
    lista.append(nome[:])
    nome.clear()
    notas.clear()
    op = ' '
    while op not in 'SN':
        op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break
print('-=-'*10)
print(f'{"No.":^6}{"NOME":^15}{"MÉDIA":^15}')
for c in range(0,len(lista)):
    print(f'{c:^6}{lista[c][0]:^15}{lista[c][1][2]:^15}')
while True:
    m = int(input('[999] para interromper... Mostra nota do aluno: '))
    if m == 999:
        break
    print(f'Notas de {lista[m][0]} são {lista[m][1][:2]}')
print(f'{"PROGRAMA FINALIZADO...    "}')'''
