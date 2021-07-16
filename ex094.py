lista = []
dados = {}
somaidade = 0
while True:
    dados['nome'] = input('Nome: ').strip().title()
    while True:
        dados['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('Erro. Por favor digite apenas [M] ou [F].')
    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro. Por favor digite apenas [S] ou [N].')
    if resp == 'N':
        break
print('-=-' * 11)
print(f' - Ao todo temos {len(lista)} pessoas cadastradas.')
media = somaidade / len(lista)
print(f' - A média de idade é {media:.2f}')
print(f' - As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print(f'\n - Lista de pessoas acima da idade média:')
for c in lista:
    if c['idade'] >= media:
        print(f'   > {c["nome"]} com {c["idade"]} anos.')


