dic = {}
dic['Nome'] = input('Nome: ').strip().title()
dic['Média'] = float(input(f'Média de {dic["Nome"]}: '))
if dic['Média'] <= 5:
    dic['Situação'] = 'Reprovador'
elif dic['Média'] <= 6.9:
    dic['Situação'] = 'Recuperação'
else:
    dic['Situação'] = 'Aprovado'
print('-=-' * 5)
for k, v in dic.items():
    print(f' -- {k}: {v}')


