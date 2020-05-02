from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador PENSAR
print('\33[33m-=-\33[m' * 20)
print('\33[36mVou pensar um número entre 0 e 5. Tente adivinhar...\33[m')
print('\33[33m-=-\33[m' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar

print('\33[31mPROCESSANDO ...\33[m')
sleep(3)

if jogador == computador:
    print('\33[34mPARABÉNS você conseguiu vencer!\33[m')
else:
    print('\33[34mGANHEI! Eu pensei no número {} e não no {}\33[m'.format(computador, jogador))
