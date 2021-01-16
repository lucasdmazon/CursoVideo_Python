contidade = 0
contmasc = 0
contfem = 0
while True:
    print('-=-' * 10)
    print('CADASTRE UMA PESSOA')
    print('-=-' * 10)
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        contidade += 1
    while True:
        sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
        if sexo == 'M' or sexo == 'F':
            break
    if sexo == 'M':
        contmasc += 1
    if sexo == 'F' and idade < 20:
        contfem += 1
    while True:
        opcao = str(input('Quer Continuar: [S/N] ')).upper().strip()[0]
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de Pessoas com mais de 18 anos: {contidade}')
print(f'Ao todo temos {contmasc} homens cadastrados')
print(f'E {contfem} mulheres tem menos de 20 anos.')
