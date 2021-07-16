def leiaint(n):
    if n.isnumeric():
        n = int(n)
    else:
        print(f'Erro! Digite um valor númerico.')

while True:
    n = input('Digite um número: ')
    leiaint(n)
    if n.isnumeric():
        n = int(n)
        print(f'O valor digitado foi {n}')
        break