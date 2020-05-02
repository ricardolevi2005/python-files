km = float(input('Soube que vai viajar, informe a distância em quilômetros: '))

if km <= 200:
    preco = km * 0.5

else:
    preco = km * 0.45

print('Para esta viagem de {:.1f}km o preço da passagem é R${:.2f}'.format(km, preco))
