idade = int(input('Digite a idade:'))
if idade <= 9:
    print('Atleta Mirim')
elif idade <= 14:
    print('Atleta Infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade <= 20:
    print('Atleta Senior')
else:
    print('Atleta Master')

'''from datetime import date
nasc = int(input('Digite seu ano  de nascimento:'))
anoatual = date.today().year
idade = anoatual - nasc
if idade <= 9:
    print('Com {} anos é pertencente a categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('Com {} anos é pertencente a categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('Com {} anos é pertencente a categoria JUNIOR.'.format(idade))
elif idade <= 25:
    print('Com {} anos é pertencente a categoria SÊNIOR.'.format(idade))
else:
    print('Com {} anos é pertencente a categoria MASTER.'.format(idade))'''