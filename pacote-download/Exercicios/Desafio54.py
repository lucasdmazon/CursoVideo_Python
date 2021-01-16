from datetime import date
maior = 0
menor = 0
ano = date.today().year
for i in range(1, 8):
    anonasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    idade = ano - anonasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoa(s) ja atingiram a maioridade e {} pessoa(s) não atingiram'.format(maior, menor))
