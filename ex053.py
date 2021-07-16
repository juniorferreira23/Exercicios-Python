frase = str(input('Digite uma frase:')).strip().upper()
separação = frase.split()
junção = ''.join(separação)
inverso = ''
#inverso = junção[::-1] # AO INVÉS DE USAR "FOR" PODE USAR CORTE DE STR
for letra in range(len(junção) - 1, -1, -1):
    inverso += junção[letra]
print(f'O inverso de {junção} é {inverso}')
if junção == inverso:
    print('Esta frase é um PALÍNDROMO')
else:
    print('Esta frase não é um PALÍNDROMO')