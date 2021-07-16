def ficha(jogador, gols):
    if jogador.strip() == '':
        jogador = 'Desconhecido'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    dados = print(f'O jogador <{jogador}> fez {gols} gols no campeonato')


j = input('Nome do Jogador: ').title().strip()
g = input('Número de gols: ')

ficha(j,g)