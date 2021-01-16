escol = 1
cont = soma = maior = menor = 0
while escol == 1:
    n = int(input('Digite um valor: '))
    escol = int(input('''SIM - 1
NÂO - Qualquer numero
Quer continuar: '''))
    cont += 1
    soma += n

    if maior == 0:
        maior = n
    if n > maior:
        maior = n

    if menor == 0:
        menor = n
    if n < menor:
        menor = n

media = soma / cont
print('A média dos numeros lidos é {:.2f}, o maior valor é {} e o menor valor é {}.'.format(media, maior, menor))