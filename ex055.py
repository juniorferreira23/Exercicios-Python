maior = 0
menor = 0
for pessoas in range(1,6):
    peso = float(input(f'Qual o peso da {pessoas}º pessoa? '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')