from random import randint
n = []

def sortear(lst):
    print(f'Sorteando 5 valores da lista:',end=' ')
    for c in range(0,5):
        n = randint(1,10)
        lst.append(n)
        print(f'{n}', end=' ')
    print('Pronto!')


def somapar(lst):
    s = 0
    for c in lst:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {lst}, temos: {s} ')


sortear(n)
somapar(n)
