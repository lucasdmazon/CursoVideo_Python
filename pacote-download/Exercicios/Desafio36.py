valcasa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o valor do seu salario: R$'))
anos = int(input('Digite em quantos anos voce vai pagar este emprestimo: '))
emp = valcasa / anos
emp = emp / 12
if sal * 30/100 <= emp:
    print('Você tera que pagar R${:.2f} por mês, você infelizmente não pode pagar por esta prestação'.format(emp))
else:
    print('Você tera que pagar R${:.2f} por mês'.format(emp))