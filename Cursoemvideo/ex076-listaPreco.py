from colorama import Fore, init
init()
cores = {
    'amarelo': Fore.YELLOW,
    'azul': Fore.BLUE,
    'vermelho': Fore.RED,
    'verde': Fore.GREEN,
    'roxo': Fore.MAGENTA,
    'ciano': Fore.CYAN, 
    'reset': Fore.RESET
}

lista = ('Pão', 0.50, 'teclado', 120.00, 'mochila', 50.00, 'biscoito', 5.00, 'camisa', 45.00,
'som', 399.99, 'azeite', 29.99, 'caneta', 3.00)

print(f'{cores["vermelho"]}~='*16)
print('{:^32}'.format('MERCADO DO KAYAN'))
print('~='*16)
for c in range(0,(len(lista))):
    if c % 2 == 0:
        print(f'{cores["reset"]}{lista[c]}','.'*(20 - (len(lista[c])-2)), (f'R${lista[c+1]:.2f}'))
print('~='*16)
