a = float(input('{}Qual o preço do produto? R$ {}'.format('\033[1;34m', '\033[m')))
por = a * 5/100
na = a - por
print('{}Havera 5% de desconto portanto o preço mudara de R${} para R${:.2f} '.format('\033[1;30m', a, na))