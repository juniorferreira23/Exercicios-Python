nome = str(input('Digite seu nome completo:')).strip()
dividido = nome.split()
print('Analisando seu nome...')
print('O nome em maiúsculo é: {}'.format(nome.upper()))
print('O nome em minúsculo é: {} '.format(nome.lower()))
print('O total de letras do seu nome é: "{}", sem considerar espaços'.format(len(nome) - nome.count(' ')))
# format(len(nome) - nome.count(' ')) é: ler nome - quantos espaços foram encontrados
print('O seu primeiro nome é {} e possui {} letras'.format(dividido[0],len(dividido[0][0:])))

# MINHA VERSÃO
#nome = str(input('Digite seu nome completo:')).strip()
#dividido = nome.split()
#junção = (''.join(dividido))
#print('O nome em maiscúlo é {}'.format(nome.upper()))
#print('O nome em minuscúlo é {}'.format(nome.lower()))
#print('O total de letras sem considerar espaços é: {}'.format(len(junção)))
#print('O seu primeiro nome é {} e tem {} letras'.format(dividido[0],len(dividido[0][0:])))