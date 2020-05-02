from math import hypot

co = int(input('Informe o valor do cateto oposto: '))
ca = int(input('Informe o valor do cateto adjacente: '))

#co2 = pow(co,2)
#ca2 = pow(ca,2)

#hip = math.sqrt(co2 + ca2)

hi = hypot(co,ca)

print('Para cateto oposto ={} e cateto adjacente={} temos hipotenusa={}'.format(co, ca,  hi))



