escolha = 0
print('\033[31m-----------------\033[m')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while escolha != 5:
    print('''
\033[34mEscolha a opção:
[1] Somar
[2] Subtrair
[3] Maior
[4] Novos números
[5] Sair do programa\033[m''')
    escolha = int(input('Opção: '))
    if escolha == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif escolha == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O mairo número é {n2}')
    elif escolha == 4:
        print('')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif escolha == 5:
        print('\033[36m---Finalizando o programa---\033[m')
    else:
        print('\033[31mOpção inválida, tente novamente...\033[m')

