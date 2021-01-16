'''
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
galera = [['joão', 19], ['ana', 33], ['joaquin', 13], ['maria', 45]]
print(galera[0][1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

galera = list()
dado = list()
totm = 0
totme = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totm += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totme += 1
print(f'Temos {totm} maiores e {totme} menores de idade.')
