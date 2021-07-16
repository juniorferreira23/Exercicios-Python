jogador = {}
gols = []
s = 0
jogador['nome'] = input('Nome do jogador: ').strip().title()
partidas = int(input(f'Quantidades de partidas de {jogador["nome"]}: '))
for p in range(0,partidas):
    gols.append(int(input(f'Quantos gols na {p + 1}º partida? ')))
jogador["gols"] = gols[:]
jogador["total"] = sum(jogador["gols"])
print('-=-' * 10)
print(jogador)
print('-=-' * 10)
for k, v in jogador.items():
    print(f'{k} tem valor de: {v}')
print('-=-' * 10)
for i, n in enumerate(jogador["gols"]):
    print(f'   => No {i + 1}º jogo fez {n}')
print(f'   => Total de gols é {jogador["total"]}')
print('-=-' * 10)