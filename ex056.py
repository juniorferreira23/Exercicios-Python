somaidade = 0
maioridadehomem = 0
nomevelho = ''
cont = 0
for pessoas in range(1,5):
    print('----{}º Pessoa-----'.format(pessoas))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))#.upper() utilizei outro metodo na condição coloquei "in"
    somaidade += idade
    média = somaidade / 4   #SOLUCÃO DA PRIMEIRA QUESTÃO
    if pessoas == 1 and sexo in 'Mm': #SOLUÇÃO DA SEGUNDA QUESTÃO #Viu o uso do in, não precisei da upper
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff':    #SOLUÇÃO DA TERCEIRA QUESTÃO #Viu o uso do in, não precisei da upper
        if idade < 20:
            cont += 1
print('')
print(f'A média de idade do grupo é de {média} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'A quantidade de mulheres com menos de 20 anos é {cont}')