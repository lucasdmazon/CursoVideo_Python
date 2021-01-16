expressao = str(input('Digite a expressão: '))
expressao = list(expressao)
for i in expressao:
    if i == '(':
        for i in expressao:
            if i == ')':
                expressao.remove('(')
                expressao.remove(')')
if '(' in expressao or ')' in expressao:
    print('Sua expressão está errada!')
else:
    print('Sua expressão está Valida!')
