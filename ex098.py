def contador(i,f,p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1

    print('-' * 30)
    print(f'Contador de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
        print('Pronto!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
        print('Pronto!')

contador(0,10,1)
contador(10,0,-2)
print('-'*30)
print('Agora é a sua vez de personalizar o contador!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)