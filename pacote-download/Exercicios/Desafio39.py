from datetime import date
sexo = str(input('Sigite H para homem M para mulher: '))
anonasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
tempo = 18 - idade
anofutur = anoatual + tempo
anopas = anoatual - (idade - 18)
if idade < 18 and sexo == 'H':
    print('Você esta com {} anos, você  deve se alistar no serviço militar daqui {} ano(s) no ano de {}'.format(idade, tempo, anofutur))
elif idade == 18 and sexo == 'H':
    print('Você esta com {} anos, esta na hora de se alistar'.format(idade))
elif idade > 18 and sexo == 'H':
    tempo = idade - 18
    print('Você esta com {} anos, ja passou da época de se alistar a {} ano(s) no ano de {}'.format(idade, tempo, anopas))
elif sexo == 'M':
    print('Você não precisa se alistar')
else:
    print('Houve um erro de digitação')