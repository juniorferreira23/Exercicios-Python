#for c in range(1,501):
#    if c % 3 == 0:
#        print(c)
soma = 0
cont = 0
for c in range(3,501,3):
    if c % 2 == 1:
        print(c)
        soma = soma + c
        cont = cont + 1
print(f'A soma de todos os {cont} valores é: {soma}')