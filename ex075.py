n = (int(input('Digite um número: ')),int(input('Digite outro número: ')),
     int(input('Digite mais número: ')),int(input('Digite um último número: ')))
print('-' * 20)
print(f'O número "9" foi digitado [{n.count(9)}] vezes.')
if 3 in n:
    print(f'O número "3" apareceu na posição: [{n.index(3) + 1}]')
else:
    print('O número "3" não foi encontrado.')
print('Os valores PARES digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c}', end='  ')