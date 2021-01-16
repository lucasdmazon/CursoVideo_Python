from time import sleep


def maior(* val):
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    sleep(2)
    for i in val:
        print(i, end=' ')
        sleep(0.5)
        if maior == 0 or i > maior:
            maior = i
    print(f'Foram informados {len(val)} valores ao todo')
    print(f'O maior valor imformado foi {maior}.')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
