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

n = 0
contagem = 0
while n < 999:
    soma = int(input('\nInforme a quantidade que deseja: '))
    n += soma
    contagem += 1
    if n >= 999:
        contagem -= 1
print(f'\n{cores["amarelo"]}Você informou {contagem} números!!')
print(f'E a soma deles foi de {n} {cores["reset"]}')