from random import randint
from time import sleep
print('-=-'*19)
print('|Vou pensar em um número entre 0 e 5. Tente adivinhar...|')
print('-=-'*19)
random = randint(0,5)
n = int(input('Em qual número eu pensei:'))
print('PROCESSANDO...')
sleep(2)
if n == random:
    print('Parabén! você acertou!')
else:
    print('Você errou! O número em que eu pensei foi "{}", mas sorte na próxima!'.format(random))
print('----FIM DE JOGO----')
