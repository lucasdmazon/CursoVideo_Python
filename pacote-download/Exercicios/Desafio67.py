while True:
    print('-' * 30)
    n = int(input('Qual tabuada você quer ver? '))
    print('-' * 30)
    if n < 0:
        break
    for i in range(0, 11):
        mult = i * n
        print(f'{n} x {i} = {mult}')
print('Tabuada Encerrada, volte sempre!')
