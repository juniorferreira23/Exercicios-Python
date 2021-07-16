lista = []
jogador = {}
gols = []
s = 0
while True:
    jogador['nome'] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantidades de partidas de {jogador["nome"]}: '))
    for p in range(0,partidas):
        gols.append(int(input(f'Quantos gols na {p + 1}º partida? ')))
    jogador["gols"] = gols[:]
    jogador["total"] = sum(jogador["gols"])
    lista.append(jogador.copy())
    gols.clear()
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro. Por favor digite apenas [M] ou [F]')
    if resp == 'N':
        break
print('-=-' * 11)
print(f'{"Cod.":<4}', end='')
for c in jogador.keys():
    print(f'{c:^10}', end='')
print()
for i, v in enumerate(lista):
    print(f'{i:^4}', end='')
    for d in v.values():
        print(f'{str(d):^10}', end='')
    print()
print('\n','-=-' * 11)
while True:
    busca = int(input('(999) para parar. Mostrar dados de qual jogador: '))
    if busca == 999:
        break
    elif busca <= len(lista) - 1:
        print(f' - Levantamento do jogador {lista[busca]["nome"]}')
        for i, n in enumerate(lista[busca]['gols']):
            print(f'   > Na {i + 1}º partida foi feito {n} gols')
    else:
        print(f'Erro. Não existe jogador {busca}')

print(lista)