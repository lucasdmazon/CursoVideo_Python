sal = float(input('{}Qual seu salario atual? R$ '.format('\033[1;35m')))
if sal > 1250.00:
    aum = sal * 10/100
else:
    aum = sal * 15/100
saln = sal + aum
print('{}O seu novo salario sera de R${:.2f}'.format('\033[1;30m', saln))