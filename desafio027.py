nome = str(input('Digite seu nome completo: ')).strip()

n = nome.split()

print('Um prazer te conhecer {}'.format(nome.title()))
print('Seu primeiro nome é {} '.format(n[0].title()))
print('Seu último nome é {}'.format(n[len(n)-1].title()))
