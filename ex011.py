altura = float(input('Digite a altura em metros:'))
largura = float(input('Digite a largura em metros:'))
area = altura * largura
pintura = area / 2
print('A área é: {:.2f}M, será necessario {:.2f}L de tinta.'.format(area,pintura))
print('Considerando que 1L de tinta pinta 2M.')
