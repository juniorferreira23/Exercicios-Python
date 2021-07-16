nome = str(input('Digite seu nome:')).strip()
nome = nome.title()
print('O nome "{}" possui o sobrenome "Silva"?'.format(nome),('Silva' in nome))