peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite sua altura (M): '))
imc = peso / altura ** 2
print('Seu Indice de Massa Corporea é de {:.1f} '.format(imc), end='')
if imc < 18.5:
    print('você está abaxo do peso')
elif imc >= 18.5 and imc < 25:
    print('você esta no peso ideal')
elif imc >= 25 and imc < 30:
    print('você esta sobrepeso')
elif imc >= 30 and imc <= 40:
    print('você esta na obesidade')
else:
    print('você esta na obesidade mórbida')