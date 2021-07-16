sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
if sexo != 'M' and sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        print('\033[31mOpção inválida, digite uma opção possível.\033[m')
        sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
print('Obrigado, dado registrado com sucesso!')
