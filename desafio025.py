nome = str(input('Digite o seu nome completo: ')).strip().lower()

nome.find('silva') == -1

print('Seu nome tem Silva? {}'.format(nome.find('silva') != -1))

