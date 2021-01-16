def area(larg, comp):
    print(f'A área de um terreno de {larg:}x{comp:} é de {larg*comp:}m²')


print('Controle de Terrenos')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
