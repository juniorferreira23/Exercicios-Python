lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if escolha in 'SN':
            print('-' * 20)
            break
        else:
            print('\033[31mOpção inválida, tente novamente.\033[m')
    if escolha == 'N':
        break
for v in lista:
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
print(f'A lista dos valores: {sorted(lista)}')
print(f'Lista dos valores PARES: {sorted(lista_par)}')
print(f'Lista dos valores IMPARES: {sorted(lista_impar)}')