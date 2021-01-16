soma = 0
cont = 0
for i in range(1, 7):
   a = int(input('Digite o {}º valor: '.format(i)))
   if a % 2 == 0:
       soma += a
       cont += 1
print('A soma de todos os {} pares digitados é de: {}'.format(cont, soma))
