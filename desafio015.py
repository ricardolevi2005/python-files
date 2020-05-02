km = float(input('Informe a quantidade de km rodados: '))
dias = int(input ('Informe a quantidade de dias com o carro: '))
precokm = float(0.15)
diaria = 60
valor = (km * precokm) + (dias * diaria)
print('O preço a pagar pelos {} dias com o carro e {}km rodados é de R${:.2f}'. format(dias, km, valor))
