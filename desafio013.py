s = float(input('O salário inicial é de: R$'))
a = 15
ns = (s * (1 + a / 100))
print('O salário com aumento de {}% é: R${:.2f}'.format(a, ns))
