print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)
n = int(input('Digite quantos termos deseja mostrar: '))
n_ant = 0
num = 1
while n >= 0:
    print(f'{num}',end=' -> ')
    num = num + n_ant
    n_ant = num - n_ant
    n -= 1
print('FIM')