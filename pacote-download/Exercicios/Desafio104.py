def leiaInt(valor):
    while True:
        num = input(valor).strip()
        if num.isnumeric() == True:
            return num
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
