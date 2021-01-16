sal = float(input('{}Digite seu salario: R$ '.format('\033[1;36m')))
por = sal * 15/100
saln = sal + por
print('{}Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format('\033[1;30m', sal, saln))