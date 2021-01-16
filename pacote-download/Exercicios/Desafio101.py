from datetime import datetime


def voto(anonasc):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - anonasc
    if idade < 18:
        return 'VOTO NEGADO'
    elif idade <= 65:
        return'VOTO OBRIGATORIO'
    else:
        return'VOTO OPCIONAL'


print('-'*30)
anonasc = int(input('Em que ano você nasceu? '))
ano = datetime.now().year
idade = ano - anonasc
print(f'Com {idade} anos: ', end='')
print(voto(anonasc))
