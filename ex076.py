tupla = ('Notebook',3299.00,'Celular',1200.00,
         'Pc Gamer',3500.00,'Fone',89,'Nintendo Switch',2900.00)
for c in range(0, len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:.<30}', end='')
    else:
        print(f'R${tupla[c]:>10.2f}')