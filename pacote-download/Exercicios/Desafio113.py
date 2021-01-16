def leiaInt(mens):
    while True:
        try:
            num = int(input(mens))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            num = 0
            break
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return num


def leiaFloat(mens):
    while True:
        try:
            num = float(input(mens))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.')
            num = 0
            break
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return num


n = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {n2}')



'''
def leiaInt(mens):
    while True:
        num = input(mens).strip()
        if num.isalpha() == True:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            try:
                num = int(num)
            except KeyboardInterrupt:
                print('\033[31mUsuário preferiu não digitar esse número.\033[m')
                num = 0
                break
            except:
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            else:
                break
    return num


def leiaFloat(mens):
    while True:
        num = input(mens)
        if num.isalpha() == True:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            try:
                num = float(num)
            except KeyboardInterrupt:
                print('\033[31mUsuário preferiu não digitar esse número.')
                num = 0
                break
            except:
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            else:
                break
    return num


n = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {n2}')
'''