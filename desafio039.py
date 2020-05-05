from datetime import date

nasc = int(input('Informe o ano de seu Nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, anoatual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento será em {}.'.format(anoatual+(18-idade)))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos'.format(idade-18))
    print('Seu alistamento foi em {}.'.format(anoatual-(idade-18)))
else:
    print('Você tem que se alistar IMEDIANTAMENTE')


