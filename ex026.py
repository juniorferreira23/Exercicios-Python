frase = str(input('Digite uma frase:')).strip().upper()
print('A quantidade de vezes que aparece a letra "A" é: {}'.format(frase.count('A')))
print('A primeira posição do "A" é: {}'.format(frase.find('A') + 1))
print('A ultima posição do "A" é: {}'.format(frase.rfind('A') + 1))
# Observação: esse " + 1 " é para não da localização errada já que o python reconhece zero "0"