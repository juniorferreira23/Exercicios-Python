from random import randint
computador = randint(1,10)
cont = 0
print('{:=^26}'.format('JOGO'))
print('-=-' * 9)
print('{}ACERTE O NÚMERO DE 1 A 10!{}'.format('\033[32m','\033[m'))
print('-=-' * 9)
escolha = int(input('Em qual número eu pensei? '))
if escolha != computador and escolha >= 1 and escolha <= 10:
    while escolha != computador:
        escolha = int(input('Você ainda não acertou, tente novamente: '))
        cont += 1
        if escolha < 1 or escolha > 10:
            print('{}Escolha inválida, as opções são entre 1 a 10. Tente novamente.{}'.format('\033[31m','\033[m'))
        if escolha < computador:
            print('\033[32mMais...\033[m')
        elif escolha > computador:
            print('\033[32mMenos...\033[m')
elif escolha < 1 or escolha > 10:
    print('{}Escolha inválida, as opções são entre 1 a 10. Tente novamente.{}'.format('\033[31m','\033[m'))
    while escolha != computador:
        escolha = int(input('Você ainda não acertou, tente novamente: '))
        cont += 1
        if escolha < 1 or escolha > 10:
            print('{}Escolha inválida, as opções são entre 1 a 10. Tente novamente.{}'.format('\033[31m','\033[m'))
        if escolha < computador:
            print('\033[32mMais...\033[m')
        elif escolha > computador:
            print('\033[32mMenos...\033[m')
print('\033[32m--------------------------------------------------\033[m')
print(f'Parabéns você acertou! O número de tentativas foi {cont + 1}')
if (cont + 1) > 5:
    print('Você levou muitas tentativas até acertar, você é muito ruim no jogo xD!')

#Versão Guanabará
'''from random import randint
computador = randint(1,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Você consegue advinhar qual foi o número?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print(f'Parabéns você acertou em {palpites} tentativas')'''