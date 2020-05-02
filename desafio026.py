frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra "a" aparecere {} vezes'.format(frase.count('a')))
print('Ela aparece a primeira vez na posicao {}'.format(frase.find('a')+1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('a')+1))
