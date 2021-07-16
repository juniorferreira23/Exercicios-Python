num = int(input('Digite um número: '))
print('-=-'*6)
print(f'A tabuada de {num} é:')
print('-=-'*6)
for c in range(1,11):
    print(f'{num} x {c} = {num * c}')