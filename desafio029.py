vel = float(input('Que velocidade você está trafegando(km)? '))

if vel > 80:
    print('Você foi MULTADO por ter ultrapassado a velocidade máxima de 80km/h')
    multa = (vel - 80)*7.0
    print('O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! DIRIJA COM SEGURANÇA!')
