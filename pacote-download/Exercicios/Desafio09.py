larg = float(input('{}Digite a largura da parede: '.format('\033[1;31m', '\033[m')))
alt = float(input('Digite a altura da parede: {}'.format('\033[m')))
area = larg * alt
tinta = area/2
print('{}Sua parede tem a dimenção de {}x{}, a área é de {}m² e serão necessarios {}l de tinta.'.format('\033[1;30m', larg, alt, area, tinta))