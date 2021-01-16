dados = []
lista = []
maior = menor = 0
while True:
    lista.append(str(input('Digite um nome: ')))
    lista.append(float(input('Digite seu peso: ')))
    while True:
        escol = str(input('Quer continuar?[S/N] ')).upper().split()[0]
        if escol in 'SN':
            break
    dados.append(lista[:])
    lista.clear()
    if escol in 'N':
        break
print('-='*30)
print(f'{len(dados)} pessoas foram cadastradas.')

for c in dados:
    if maior == 0 or c[1] > maior:
        maior = c[1]
    if menor == 0 or c[1] < menor:
        menor = c[1]

print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for i in dados:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print('\n')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for a in dados:
    if a[1] == menor:
        print(f'[{a[0]}]', end='')
