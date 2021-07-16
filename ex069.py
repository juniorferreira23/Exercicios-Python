maior_18 = homem = mulheres_menor_20 = 0
print('-' * 20)
print('CADASTRO DE USUÁRIOS')
print('-' * 20)
while True:
    idade = int(input('Digite a idade do usuário: '))
    if idade >= 18:
        maior_18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            mulheres_menor_20 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('-' * 20)
    if escolha == 'N':
        break
print(f'O número de usuários maiores de 18 anos foram [{maior_18}]')
print(f'O número de homens cadastrados foram [{homem}]')
print(f'O número de mulheres cadastradas menores de 20 anos foram [{mulheres_menor_20}]')
