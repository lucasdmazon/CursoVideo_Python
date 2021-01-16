print('-' * 40)
print('{:^40}'.format('LoJA SUPER BARATÃO'))
print('-' * 40)
total = contpreco = menor = 0
nomemenor = ''
while True:
    nome = str(input('Nome: ')).strip()
    preco = int(input('Preço: R$'))
    total += preco
    if preco >= 1000:
        contpreco += 1
    if menor == 0 or preco < menor:
        menor = preco
        nomemenor = nome
    while True:
        escol = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
        if escol == 'S' or escol == 'N':
            break
    if escol == 'N':
        break
print('-' * 20, 'FIM DO PROGRAMA', '-' * 20)
print(f'O total da compra foi de R${total:.2F}')
print(f'Temos {contpreco} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemenor} que custa R${menor:.2F}')
