from random import randint
print('-=-' * 11)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-' * 11)
vitoria = 0
while True:
    computador = randint(1, 10)
    print('-' * 20)
    jogador = int(input('Digite um número: '))
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('IMPAR OU PAR? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou [{jogador}] e o computador [{computador}]... [{total}]', end=' ')
    print('é PAR' if total % 2 == 0 else 'é IMPAR')
    if total % 2 == 0:
        if escolha in 'Pp':
            print('\033[32mParabéns! Você venceu essa rodada.\033[m')
            vitoria += 1
        elif escolha in 'Ii':
            print('\033[31mVocê Perdeu!\033[m :(')
            break
    if total % 2 == 1:
        if escolha in 'Pp':
            print('\033[31mVocê Perdeu!\033[m :(')
            break
        if escolha in 'Ii':
            print('\033[32mParabéns! Você venceu essa rodada.\033[m')
            vitoria += 1
    print('-' * 20)
print(f'\033[34mSeu total de vitorias consecutivas foi {vitoria}\033[m')