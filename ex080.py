lista = []
for c in range(0,5):
    n = int(input(f'Digite um valor: '))
    if c == 0 or n > lista[-1]: #lista[-1] significa: o ultimo item da lista lembra de trás para frente
        lista.append(n)
        print('\033[34mAdicionado ao final da lista.\033[m')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'\033[34mAdicionado na posição {pos}\033[m')
                break
            pos += 1
print(f'Os valores digitados foram: {lista} ')