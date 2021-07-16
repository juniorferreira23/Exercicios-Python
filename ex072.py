tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num >= 0 and num <= 20:
            print(f'O número digitado foi {tupla[num]}')
            break
        else:
            print('\033[31mOpção inválida, tente novamente...\033[m')
    while True:
        escolha = str(input('\033[34mDeseja continuar? [S/N]: \033[m')).strip().upper()[0]
        if escolha in 'SN':
            print('-' * 20)
            break
        else:
            print('\033[31mOpção inválida, tente novamente...\033[m')
    if escolha == 'N':
        break

