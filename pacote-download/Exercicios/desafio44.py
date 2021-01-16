print('{:=^40}'.format(' Lojas Mazon '))
preço = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
con = int(input('Digite a condição de pagamento: '))
if con == 1:
    des = preço - (preço * 10/100)
elif con == 2:
    des = preço - (preço * 5/100)
elif con == 3:
    des = preço
    parcela = preço / 2
    print('Sua compra sera parcelada em 2x de {:.2f}'.format(parcela))
elif con == 4:
    des = preço + (preço * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = preço / totalparc
    print('Sua compra sera parcelada em {}x de R${:.2f} com juros'.format(totalparc, parcela))
else:
    preço = 0
    des = 0
    print('{}OPÇÃO INVALIDA de pagamento. Tente Novamente!'.format('\033[1;31m'))
print('O valor a ser pago por sua compra de {:.2f} sera de R${:.2f}'.format(preço, des))