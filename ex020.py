from random import shuffle
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')
lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
#Não sei o porque, mas não dá para colocar o shuffle na formatação
print('A ordem de apresentação sorteada foi: {}'.format(lista))
