n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Média: {:.1f}'.format(m))
if m < 5.0:
    print('REPROVADO')
elif m >= 5.0 and m <= 6.9:
    print('RECUPERAÇÃO')
elif m >= 7.0 and m <= 10:
    print('APROVADO')
else:
    print('valor invalido')