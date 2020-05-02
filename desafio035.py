

a = float(input('Informe o primeiro segmento de reta: '))
b = float(input('Informe o segundo segmento de reta: '))
c = float(input('Informe o terceiro segmento de reta: '))

#  |b-c|<a<b+c
if ((a < b+c) and (a > (b - c)*-1)) or ((b < a+c) and (b > (a - c)*-1)) or ((c < b+a) and (c > (b - a)*-1)):
    print('Estes segmentos podem formar um triângulo!')
else:
    print('Estes segmentos não podem formar um triângulo!')
