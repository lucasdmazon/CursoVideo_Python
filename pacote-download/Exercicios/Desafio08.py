a = float(input('{}Digite o seu dinheiro: R${}'.format('\033[1;36m', '\033[m')))
b = a/5.63
print('{}Com R${} você pode comprar U${:.2f} dolares'.format('\033[1;30m', a, b))
