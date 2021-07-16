total = maior_qmil = menor_preço = cont = 0
nome_menorp = ' '
print('-' * 20)
print('CADASTRO DE PRODUTOS')
print('-' * 20)
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto R$: '))
    cont += 1
    total += preço  # Contando para somar os preços
    if preço > 1000:    # Metodo para calcular preços maior que mil reias
        maior_qmil += 1
    if cont == 1 or preço < menor_preço:   # Metodo para calcular o preço do produto mais caro
        menor_preço = preço
        nome_menorp = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('-' * 20)
    if escolha == 'N':
        print('-------RESULTADO-------')
        break
print(f'O total gasto na compra foi R$:{total}')
print(f'O número de produtos que custam mais que mil reais foram: [{maior_qmil}]')
print(f'O produto mais barato foi: "{nome_menorp}" custando R$:{menor_preço}')

# Versão para se o usuário fugisse das respostas convencionais do input escolha:
#    if escolha != 'S' and escolha != 'N':
#        while escolha != 'S' and escolha != 'N':
#            print('\033[31mOpção inválida, Tente novamente.\033[m')
#            escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]