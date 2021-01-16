vel = int(input('{}Digite a velocidade do carro: '.format('\033[1;33m')))
if vel > 80:
    multa = (vel - 80) * 7
    print('{}Você foi multado por exceder o limite de 80Km/h em R${:.2f}, va mais devagar!'.format('\033[1;31m', multa))
else:
    print('{}Sua velocidade esta dentro do limite permitido. Dirija com segurança!'.format('\033[1;36m'))