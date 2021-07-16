cidade = str(input('Digite o nome da sua cidade:')).strip()
cidade = cidade.title()
cid = cidade.split()
print('A cidade "{}" começa com o nome "Santo"?'.format(cidade),('Santo' in cid[0]))

# Versão Guanabara
#cid = str(input('Digite o nome da sua cidade:')).strip()
#print(cid[:5].title() == 'Santo')