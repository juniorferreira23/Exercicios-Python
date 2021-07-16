def notas(*n, sit=False):
    dic = {}
    dic['Total'] = len(n)
    dic['Maior Nota'] = max(n)
    dic['Menor Nota'] = min(n)
    dic['Média'] = sum(n) / len(n)
    if sit:
        if dic['Média'] < 5:
            dic['Situação'] = 'RUIM'
        elif dic['Média'] < 7:
            dic['Situação'] = 'RAZOÁVEL'
        else:
            dic['Situação'] = 'BOA'
    return print(f'{dic}')


notas(7.4,5.6,3.4,7.5, sit=True)