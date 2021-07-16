'''fatorial = int(input('Digite um número para calcular o seu fatorial: '))
multiplicador = 1
print(f'O fatorial de {fatorial}! = ',end=' ')
while fatorial >= 1:
    print(fatorial, end=' ')
    print('x' if fatorial > 1 else '=',end=' ')
    multiplicador *= fatorial
    fatorial -= 1
print(f'{multiplicador}')'''

f = int(input('Digite um número para calcular o seu fatorial: '))
m = 1
print(f'O fatorial de {f}! = ',end='')
for c in range(f, 0, -1):
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    m *= c
print(f'{m}')
