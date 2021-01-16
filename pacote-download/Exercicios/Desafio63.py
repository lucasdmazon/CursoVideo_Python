print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos voce quer mostrar: '))
f1 = 0
f2 = 1
print('~'*30)
print('{} -> {}'.format(f1, f2), end='')
cont = 3
while cont <= n:
    fib = f1 + f2
    print(' -> {}'.format(fib), end='')
    f1 = f2
    f2 = fib
    cont += 1
print(' -> Fim')
