n = int(input('Digite um número inteiro:'))
print('''Escolha a base da conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Escolha uma opção:'))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {} '.format(n,bin(n)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')