from math import hypot
co = float(input('Digite o comprimento do cateto oposto em Cm:'))
ca = float(input('Digite o comprimento do cateto adjacente em Cm:'))
hipotenusa = hypot(co,ca)
#hipotenusa = sqrt((co**2) + (ca**2))
#hipotenusa = (co**2 + ca**2) **(1/2) < Raiz quadrada
print('A hipotenusa vai medir:{:.2f}Cm'.format(hipotenusa))
