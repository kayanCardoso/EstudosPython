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

print(f'{cores["ciano"]}#'*30)
# uso do format para alinhar string
print('{:^30}'.format('BANCO DO KAYAN'))
print(f'#'*30)
valor = int(input(f'{cores["reset"]}Qual valor será sacado ? R$'))
ced = valor // 50
if ced >= 1:
    print(f'Disponivel {ced} cédulas de R$50')
rest = valor % 50 
ced = rest // 20
if ced >= 1:
    print(f'Disponivel {ced} cédulas de R$20')
rest = rest % 20
ced = rest // 10
if ced >= 1:
    print(f'Disponivel {ced} cédulas de R$10')
ced = rest % 10
if ced >= 1:
    print(f'Disponivel {ced} cédulas de R$1')