dados = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}° numero: '))
    if n % 2 == 0:
        dados[0].append(n)
    else:
        dados[1].append(n)
print('-=' * 30)
print(f'Os valores pares digitados foram {sorted(dados[0])}')
print(f'Os valores impares digitados foram {sorted(dados[1])}')
