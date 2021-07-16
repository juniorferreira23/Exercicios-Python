n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media < 5.0:
    print('Você está {}Reprovado!{} Sua média({}) foi abaixo do limite(7.0).'.format('\033[31m','\033[m', media))
elif 6.9 >= media >= 5.0:
#elif media >= 5.0 and media <= 6.9:
    print('Você está em {}Recuperação!{} Com sua média({}) não foi possível bater o necessário.'.format('\033[31m', '\033[m', media))
else:
    print('Parabéns você está {}Aprovado!{} Sua média({}) ultrapassou ou igualou o exigido(7.0).'.format('\033[32m','\033[m',media))