#2º VERSÃO SEM GAMBIARRA, USANDO CONTADOR E WHILE TRUE PARA VERIFICAR SE TEM NÚM. REPITIDOS
from random import randint
from time import sleep
lista = []
palpites = []
total = 0
quant = int(input('Quantos jogos deseja sortear? '))
while total < quant:
    cont = 0
    while True:
        v = randint(1,60)
        if v not in palpites:
            palpites.append(v)
            cont += 1
        if cont == 6:
            break
    lista.append(palpites[:])
    palpites.clear()
    total += 1
for p, c in enumerate(lista):
    print(f'{p + 1}º Jogo: {c}')
    sleep(1)

#MINHA 1º VERSÃO ONDE EU SORTEI DEZ NÚMERO PARA CASO TENHA NÚMERO REPITIDO E SELICIONO OS 6 PRIMEIROS
'''from random import randint
from time import sleep
lista = []
palpites = []
op = int(input('Quantos jogos deseja sortear? '))
for c in range(0,op):
    for n in range(0,10):
        v = randint(1,60)
        if v not in palpites:
            palpites.append(v)
    lista.append(palpites[:6])
    palpites.clear()
for c in range(0,len(lista)):
    lista[c].sort()
    print(f'Jogo {c + 1}º :{lista[c]}')
    sleep(1)'''