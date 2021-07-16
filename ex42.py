print('-=-'*20)
print('|Forme um triângulo com a medição do seguimento de três retas|')
print('-=-'*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Secundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Com esses segmentos é possível formar um triângulo!')
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓSCELES')
else:
    print('Com essas medidas não é possível formar um triângulo!')
