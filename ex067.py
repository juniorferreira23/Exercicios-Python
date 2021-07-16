print('-=-' * 7)
print('GERADOR DE TABUADAS')
print('-=-' * 7)
print('Digite um valor negativo para parar')
while True:
    multiplicador = 1
    n = int(input('Digite um número: '))
    print('-' * 20)
    while multiplicador >= 1 and multiplicador <= 10:
        print(f'{n} x {multiplicador} = {n * multiplicador}')
        multiplicador += 1
    print('-' * 20)
    if n < 0:
        print('\033[31mPrograma finalizado\033[m')
        break

#Versão com "for"
'''print('-=-' * 7)
print('GERADOR DE TABUADAS')
print('-=-' * 7)
print('Digite um valor negativo para parar')
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        print('\033[31mPrograma finalizado\033[m')
        break
    print('-' * 20)
    for c in range(1,11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 20)'''
