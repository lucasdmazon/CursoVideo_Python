def notas(* n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    print('-'*30)
    tupla = {}
    maior = menor = soma = 0
    tupla['total'] = len(n)
    for i in n:
        if maior == 0 or i > maior:
            maior = i
        if menor == 0 or i < menor:
            menor = i
        soma += i
    tupla['maior'] = maior
    tupla['menor'] = menor
    media = soma / len(n)
    '''
    tupla["maior"] = max(n)
    tupla["menor"] = min(n)
    media= sum(n) / len(n)
    '''
    tupla['média'] = media
    if sit:
        if media < 4.9:
            res = 'RUIM'
        elif media < 6.9:
            res = 'RAZOAVEL'
        elif media <= 10:
            res = 'BOA'
        tupla['situação'] = res
    return tupla


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
