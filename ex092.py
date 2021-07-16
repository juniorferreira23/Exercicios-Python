from datetime import date
dic = {}
dic['Nome'] = input('Nome: ').title().strip()
nasc = int(input('Ano de nascimento: '))
dic['Idade'] = date.today().year - nasc
dic['CTPS'] = int(input('[0] se não tiver. Carteira de trabalho: '))
if dic['CTPS'] != 0:
    dic['Ano de contratação'] = int(input('Ano de contratação: '))
    dic['Salário'] = float(input('Salário: R$'))
    aposentadoria = (35 - (date.today().year - dic['Ano de contratação'])) + dic['Idade']
else:
    del dic['CTPS']
print('-=-' * 11)
for k, v in dic.items():
    print(f'{k}: {v}')
if 'Ano de contratação' in dic:
    print(f'Aposentadoria com {aposentadoria} anos.')