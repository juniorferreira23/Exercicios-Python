num = int(input('Digite um número inteiro que deseje saber se ele é primo: '))
total = 0
for c in range(1,num + 1):
    if num % c == 0:
        total += 1
if total == 2:
    print('Este número é PRIMO ^^ ')
else:
    print('Este número não é PRIMO')