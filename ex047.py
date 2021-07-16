print('-=-' * 10)
print('Os números pares entre 1 e 50')
print(('-=-' * 10))
# for c in range(1, 51):  # 1 Esta maneira o laço vai ser feito 50 vezes
# if c % 2 == 0
for c in range(2, 51, 2):  # 2 Desta forma como pula de dois em dois teria menos interações.
    print(c, end=' ')  # 2 exigindo menos processamentos.
