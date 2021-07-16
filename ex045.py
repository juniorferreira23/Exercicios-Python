from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas escolhas
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Faça sua escolha: '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Escolha inválida, tente novamente.')
    quit() # Finaliza o programa, pois sem quit ele da erro com a continuação do programa
print('-=-'*9)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=-'*9)
if computador == 0:  # O computaor jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')

elif computador == 1:  # O computador jogou papel
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')

elif computador == 2:  # O computador jogou Tesoura
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
