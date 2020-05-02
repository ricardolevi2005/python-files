# nome = str(input('Digite o nome completo: '))
# #
# # print('Todas maiúsculas: {}'.format(nome.upper()))
# # print('Todas minúsculas: {}'.format(nome.lower()))
# # nome2 = nome.split()
# # junto = nome2[0]+nome2[1]+nome2[2]
# # print('Comprimento de {} é: {}'.format(junto, len(junto)))
# # primeiro = nome2[0]
# # print('O {} tem {} letras'.format(primeiro, len(primeiro)))

nome = str(input('Digite o nome completo: ')).strip()
print('Analisando seu nome...')
print('Todas maiúsculas: {}'.format(nome.upper()))
print('Todas minúsculas: {}'.format(nome.lower()))
print('Seu nome todo tem {} caracteres'.format(len(nome)))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu nome tem ao todo {} espaços'.format(nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
