a = 'BANCO CEV'
print('=' * 40)
print(f'{a:^40}')
print('=' * 40)
contA = contB = contC = contD = 0
val = int(input('Digite o valor a ser sacado: R$'))

while True:
    val -= 50
    if val < 0:
        val += 50
        break
    contA += 1
print(f'Total de {contA} cédulas de R$50')
while True:
    val -= 20
    if val < 0:
        val += 20
        break
    contB += 1
print(f'Total de {contB} cédulas de R$20')
while True:
    val -= 10
    if val < 0:
        val += 10
        break
    contC += 1
print(f'Total de {contC} cédulas de R$10')
while True:
    val -= 1
    if val < 0:
        break
    contD += 1
print(f'Total de {contD} cédulas de R$1')
print('=' * 35)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')

'''
val = int(input('Digite o valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {contC} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            breakprint('Volte sempre ao Banco CEV! Tenha um bom dia!')   
'''