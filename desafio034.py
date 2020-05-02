salario = float(input('Informe qual é o seu salário? '))
aum1 = (15/100)
aum2 = (10/100)

if salario > 1250:
    aumento = salario * (1 + (aum2))
else:
    aumento = salario * (1 + (aum1))

print('O salário para quem recebe R${} foi para R${}'.format(salario, aumento))

