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

n = 1
p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
while n != 11:
    if n == 1:
        print('A progressão é ', end='')
    print(p, end=' ')
    p += (p + r) - p
    n += 1