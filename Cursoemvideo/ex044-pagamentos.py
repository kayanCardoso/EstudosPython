preco = float(input('Informe o valor do produto:\n'))
forma = int(input('Qual a forma de pagamento ?\n\nDigite "1" para dinheiro/cheque\n"2" para Debito\n"3" para até 2x\n"4" para 3x ou mais\n'))
if forma == 1:
    print(f'O preço normal do produto é R${preco:.2f}, com desconto ficará em R${preco - (preco * 10 / 100):.2f} ')
elif forma == 2:
    print(f'O preço normal do produto é R${preco:.2f}, com desconto ficará em R${preco - (preco * 5 / 100):.2f} ')
elif forma == 3:
    print(f'O preço ficará em R${preco:.2f}, não havera descontos')
elif forma == 4 :
    print(f'O preço normal do produto é R${preco:.2f}, com juros ficará em R${preco + (preco * 20 / 100):.2f} ')
else:
    print('Opção \033[31minvalida!!!\033[m')