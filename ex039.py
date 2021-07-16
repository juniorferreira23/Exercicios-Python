from datetime import date
nascimento = int(input('Digite sua data de nascimento:'))
ano = date.today().year
if  ano - nascimento < 18:
    saldo = 18 - (ano - nascimento)
    print('Ainda não esta na hora de se alistar! você não completou 18 anos, falta {}"{} ano"{} para sua convocação.'.format('\033[31m',saldo,'\033[m'))
elif ano - nascimento == 18:
    print('Esta na hora de se alistar! Vá até a junta militar mais próximo.')
else:
    saldo = (ano - nascimento) - 18
    print('Você perdeu sua convocação para o alistamento! Está {}"{} anos"{} atrasado.\nVá até a junta militar mais próximo resolver sua situação.'.format('\033[31m',saldo,'\033[m'))

#FORMA ELABORADA QUE FIZ DE ACORDO COM O VIDEO
#from datetime import date
#ano = int(input('Digite o ano de nascimento:'))
#anoatual= date.today().year
#idade = anoatual - ano
#if idade < 18:
#    print('Quem nasce em {} tem {} anos em {}.'.format(ano,idade,anoatual))
#    print('Ainda faltam {} ano para o alistamento.'.format(18-idade))
#    print('Seu alistamento será em {}.'.format(anoatual + (18 - idade)))
    #print('Seu alistamento será em {}.'.format(ano + 17))
#elif idade == 18:
#    print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,anoatual))
#    print('Você deve ir a junta militar para se alistar!')
#else:
#    print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,anoatual))
#    print('Você deveria ter se alistado há {} anos'.format(idade - 18))
#    print('seu alistamento foi em {}'.format(ano + 17))
    #print('seu alistamento foi em {}'.format(anoatual - (idade - 18)))
