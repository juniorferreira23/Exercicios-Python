lista = []
#cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    # cont += 1  ## RESPOSTA COM CONTADOR, MAS NÃO PRECISA JÁ QUE O LEN EVITA DUAS LINHAS
    while True:
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if escolha in 'SN':
            print('-' * 20)
            break
        else:
            print('\033[31mOpção inválida, tente novamente.\033[m')
    if escolha == 'N':
        break
# print(f'A quantidade de números digitados foram [{cont}]') ## RESPOSTA COM CONTADOR
print(f'A quantidade de valores digitados foram [{len(lista)}]')
lista.sort(reverse=True)
print(f'A lista de valores em ondem decrescente: {lista}')
if 5 in lista:
    print(f'O valor "5" é encontrado na lista!')
else:
    print(f'O valor "5" não faz parte da lista.')






#VERSÃO MOSTRANDO A POSIÇÃO DE "5" DEPOIS QUE É ORDENADO EM DECRESCENTE
'''lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    while True:
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if escolha in 'SN':
            print('-' * 20)
            break
        else:
            print('\033[31mOpção inválida, tente novamente.\033[m')
    if escolha == 'N':
        break
print(f'A quantidade de números digitados foram [{cont}]')
lista.sort(reverse=True)
print(f'A lista de valores em ondem decrescente: {lista}')
if 5 in lista:
    print(f'O valor "5" é encontrado na lista na posição: ', end='')
    for pos , v in enumerate(lista):
        if v == 5:
            print(f'{pos}...', end='')
else:
    print(f'O valor "5" não faz parte da lista.')'''
