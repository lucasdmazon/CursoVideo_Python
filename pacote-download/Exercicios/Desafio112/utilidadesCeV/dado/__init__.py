def leiaDinheiro(mensagem):
    while True:
        n = input(mensagem).replace(',', '.').strip()
        a = n.replace('.', '')
        if a.isdigit() == True:
            return float(n)
            break
        else:
            print(f'\033[0;31mERRO: "{n}" é um preço inválido!\033[m')


def leiaDinheiro(mensagem):
    while True:
        n = input(mensagem).replace(',', '.').strip()
        if n.isalpha() or n == '':
         print(f'\033[0;31mERRO: "{n}" é um preço inválido!\033[m')
        else:
           return float(n)
           break

