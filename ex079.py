lista = []
while True:
    n = int(input('Digite um valor: '))     # Como mandar um númeor para lista
    if n not in lista:
        lista.append(n)
        print('\033[34mValor salvo com sucesso...\033[m')
    else:
        print('\033[31mValor duplicado, não pode ser adicionado a lista.\033[m')
    while True:
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if escolha in 'SN':
            print('-' * 20)
            break
        else:
            print('\033[31mOpção inválida, tente novamente.\033[m')
    if escolha == 'N':
        break
print(f'Os valores digitados foram: {sorted(lista)}') #Sorted - ordem e pode ser usado dentro de {}
                                                      #Ou lista.sort(), mas não vai dentro de {}
                                                      #Ordem decrescente lista.sort(reverse=True)