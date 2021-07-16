def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: Valor desejado para fatorar.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Valor do fatorial de um número n.
    """
    mult = 1
    for c in range(n, 0, -1):
        if show == True:
            print(f'{c}', 'x ' if c > 1 else '= ', end='')
        mult *= c
    if show == True:
        return print(f'{mult}')
    else:
        return print(f'O fatorial de {n} é {mult}')


fatorial(5)
fatorial(9, show=True)
help(fatorial)