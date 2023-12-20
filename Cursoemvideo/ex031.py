# Valor da viajem

km = int(input('Qual a distância da viajem ?\n'))
if km > 200:
    print(f'O preço da viajem será de R${km * 0.45:.2f}')
else:
    print(f'O preço da viajem será de R${km * 0.50:.2f}')
