from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 , 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-'*12)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('=-'*12)

if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('Você VENCEU!')
    elif jogador == 2:
        print('O Computador VENCEU!')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador == 0:
        print('O Computador VENCEU!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('Você VENCEU!')
    else:
        print('Jogada Inválida')
elif computador == 2:
    if jogador == 0:
        print('Você VENCEU!')
    elif jogador == 1:
        print('O Computador VENCEU!')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('Jogada Inválida')
