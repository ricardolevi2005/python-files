alt = float(input('Informe a altura: '))
larg = float(input('Informe a largura: '))
area = larg * alt
print('A parede de {}m x {}m tem de área {:.2f}m²'.format(larg, alt, area))
tinta = area/2
print('Será necessário {:.2f}l de tinta'.format(tinta))
