#Versão Guanabara
soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º valor:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} valores PARES é: {soma}')



#s = 0
#for c in range(1, 7):
#    num = int(input('Digite o {}º número: '.format(c)))
#    s = s + (num if num % 2 == 0 else 0) # Incrivel isso e como eu quebrei a cabeça e não conseguir entender
#print('A soma dos números PARES é: {}'.format(s)) # Ele isolou o "num" e fez a regra dentro dele .



