from time import sleep
idtotal = 0
maior = 0
nomemaior = ''
contsexo = 0
for i in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(i), '-'*5)
    nome = str(input('Nome: '.format(i)))
    idade = int(input('Idade: '.format(i)))
    sexo = str(input('[M/F]: ').upper())

    idtotal += idade

    if sexo == 'H' and idade > maior:
        maior = idade
        nomemaior = nome
    if sexo == 'M' and idade <= 20:
        contsexo += 1
media = idtotal/4
print('Analisando...')
sleep(1)
print('-'*5, 'RESULTADO', '-'*5)
print('A média de idade do gurpo é de {} anos'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(maior, nomemaior))
print('{} mulher(es) tem menos de 20 anos'.format(contsexo))