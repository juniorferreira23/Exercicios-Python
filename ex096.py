def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l}m x {c}m é {a:.1f} metros quadrados')


print('-' * 20)
print('Calculador de área')
print('-' * 20)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)