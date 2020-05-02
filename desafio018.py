from math import radians, sin, cos, tan

ang = int(input('Informe um ângulo: '))
angr = radians(ang)
s = sin(angr)
c = cos(angr)
t = tan(angr)

print('O ângulo de {}° corresponde a {:.4f} radianos'.format(ang, angr))
print('O seu SENO é {:.2f}'.format(s))
print('O seu COSSENO é {:.2f}'.format(c))
print('O sua TANGENTE é {:.2f}'.format(t))

