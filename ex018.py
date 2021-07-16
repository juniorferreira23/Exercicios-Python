from math import radians,sin,cos,tan
angulo = float(input('Digite o valor do ângulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Seno: {:.2f} , Cosseno: {:.2f} e Tangente: {:.2f}'.format(seno,cosseno,tangente))
