print('-=-'*11)
print('{}OS DEZ PRIMEIROS TERMOS DE UMA PA{}'.format('\033[36m','\033[m'))
print('-=-'*11)
termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razão
for c in range(termo,decimo + razão,razão):
    print(c, '->', end=' ')
print('Acabou')