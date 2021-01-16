lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for c in lanche:
    print(f'Eu vou comer {c}')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
print(f'Comi pra Caramba!')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')



print(sorted(lanche))

