print('{}Contador de PA{}'.format('\033[36m','\033[m'))
print('-=-' * 5)
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} > ', end=' ')
    termo += razão
    cont += 1
print('PAUSA')
