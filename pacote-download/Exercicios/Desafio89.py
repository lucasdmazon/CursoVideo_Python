lista = []
dados = []
notas = []
cont = 0
while True:
    nome = str(input('Nome: '))
    while True:
        nota1 = float(input('Nota 1: '))
        if 0 <= nota1 <= 10:
            break
    while True:
        nota2 = float(input('Nota 2: '))
        if 0 <= nota2 <= 10:
            break
    media = (nota1+nota2)/2
    '''
    lista.append([nome, [nota1, nota2], media])
    '''
    notas = [nota1, nota2, media]
    dados = [nome, notas[:]]
    lista.append(dados[:])
    cont += 1
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('-='*30)
print('No.', end=' ')
print('NOME', end='')
print(f'{"MÉDIA":^30}')
print('-'*30)
for i, v in enumerate(lista):
    print(i, end='')
    print(f'{lista[i][0]:^12}', end='')
    print(f'{lista[i][1][2]:^17.1f}')
print('-'*40)
while True:
    pesq = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if pesq == 999:
        break
    if pesq > cont:
        print('Aluno Invalido')
        break
    print(f'Notas de {lista[pesq][0]} são {lista[pesq][1][0:2]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
