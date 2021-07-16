teste = []
n = input('Digite a expressão: ').strip()
for c in n:
    if c == '(':
        teste.append(c)
    elif c == ')' and len(teste) > 0:
        teste.remove('(')
    elif c == ')' and len(teste) == 0:
        teste.append('(')
if len(teste) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está errada.')