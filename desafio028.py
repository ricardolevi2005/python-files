from random import randint
c = randint(0, 5)

n = int(input('Informe um número entre 0 e 5: '))
print('O computador escolheu {}'.format(c))

if n == c:
    print('Você venceu!')
else:
    print('Você perdeu')
