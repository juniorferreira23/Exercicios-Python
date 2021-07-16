from random import randint
from time import sleep
from operator import itemgetter
dic = {}
for c in range(1,5):
    dic[f'Jogador {c}'] = randint(1,6)
print('Valores Sorteados:')
print('-=-' * 6)
for k, v in dic.items():
    print(f'O {k} tirou [{v}]')
    sleep(1)
print('-=-' * 6)
ranking = []
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(f'Ranking dos Jogadores:')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com [{v[1]}]')
    sleep(1)


