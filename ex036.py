print('-=-'*7)
print('|Empréstimo bancário|')
print('-=-'*7)
v = float(input('Qual valor da casa que deseja comprar?'))
s = float(input('Qual o valor do seu salário:'))
a = int(input('Em quantos anos deseja pagar a casa?'))
parcela = v/ (a * 12)
s30 = s*30/100
print('')
print('"De acordo com os dados fornecidos a parcela a ser paga é de R${}{:.2f}{}/mês"'.format('\033[31m',parcela,'\033[m'))
print('"Em relação a regra de superioridade de salário 30% maior que a parcela"')
if parcela >= s30:
    print('{}"Infelizmente não poderá ser realizado o empréstimo."{}'.format('\033[31m','\033[m'))
else:
    print('{}"Parabéns! Seu empréstimo foi aprovado!"{}'.format('\033[32m','\033[m'))
