# 2º Versão
from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 17)
    print(f'Analisando os valores...')
    for valores in num:
        print(f'{valores}', end=' ')
        sleep(0.3)
        cont += 1
        if cont == 0:
            maior = valores
        else:
            if valores > maior:
                maior = valores
    print(f'Foram informados {cont} valores.')
    if cont > 0:
        print(f'O maior valor informado foi {maior}.')
    else:
        print(f'O maior valor informado foi 0.')


maior(4,5,6)
maior()

#  1º Versão
'''def maior(lst):
    print('-=' * 20)
    print('Analisando os valores passados...')
    for c in lst:
        print(f'{c}', end=' ')
    print(f'Foram informados {len(lst)} valores.')
    if len(lst) > 0:
        print(f'O maior valor informado foi {max(lst)}.')
    else:
        print(f'O maior valor informado foi 0.')


v = [2, 9, 4, 5, 7, 1]
maior(v)

v = [4, 7, 0]
maior(v)

v = []
maior(v)'''