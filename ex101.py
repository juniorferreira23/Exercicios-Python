def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NÃO OBRIGATORIO')
    elif 16 <= idade <=18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade >= 18:
        return print(f'Com {idade} anos: VOTO OBRIGATORIO')




nasc = int(input('Em que ano você nasceu? '))
voto(nasc)