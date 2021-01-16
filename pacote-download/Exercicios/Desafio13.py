t = int(input('{}Quantos dias alugados? '.format('\033[1;33m')))
km = float(input('Quantos kilometros rodados? '))
preço = (60 * t) + (0.15 * km)
print('{}O aluguel do carro vai custar R${:.2f}'.format('\033[1;30m', preço))