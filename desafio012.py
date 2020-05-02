p1 = float(input('Preço sem promoção: R$'))
desc = 5
pcd = (p1 * (1 - desc/100))
print('O valor com desconto de {}% é de R${:.2f}'.format(desc, pcd))
