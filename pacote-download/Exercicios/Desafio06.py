a = float(input('{}Digite um valor em metros: '.format('\033[1;34m')))
km = a * 0.001
hm = a * 0.01
dam = a * 0.1
dm = a * 10
cm = a * 100
mm = a * 1000
print('kilometros: {}km \nHectometros: {}hm \nDecametro: {}dam \nMetro: {}m \nDecimetro: {}dm \nCentimetro: {}cm \nMilimetro: {}mm'.format(km, hm, dam, a, dm, cm, mm))
