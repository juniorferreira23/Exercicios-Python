tupla = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Corinthians','Internacional','Goiás','Fortaleza','Bahia','Vasco da Gama','Botafogo','Atlético','Fluminense','Ceará SC','Cruzeiro','CSA','Chapecoense','Avaí')
print('-' * 100)
print(f'Os cinco primeiros colocados são:\033[34m{tupla[:5]}\033[m')
print('-' * 100)
print(f'Os ultimos quatro colocados são:\033[34m{tupla[-4:]}\033[m')
print('-' * 100)
print(f'Lista em ordem alfabetica dos times: {sorted(tupla)}')    # sorted usado para organizar em ordem alfabetica
print('-' * 100)
print(f'O time da Chapecoense encontra-se na posição:',(tupla.index('Chapecoense') + 1))

