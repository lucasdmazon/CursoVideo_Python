'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Houve um erro de digitação. Tente novamente')
print('Informação valida. Obrigado por colaborar!')
'''
sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Invalidos. Digite seu sexo[M/F]: ')).upper().strip()[0]
print('Informação valida. Obrigado por colaborar!')