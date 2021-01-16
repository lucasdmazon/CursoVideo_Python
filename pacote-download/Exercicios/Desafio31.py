num = int(input('{}Digite a distancia da viagem: '.format('\033[1;35m')))
if num <= 200:
    val = num * 0.50
else:
    val = num * 0.45
print('{}Sua viagem de {}Km custara R${:.2f}'.format('\033[1;30m', num, val))