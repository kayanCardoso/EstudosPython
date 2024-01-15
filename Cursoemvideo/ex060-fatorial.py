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

# Com biblioteca 
from math import factorial
n = -1
# while n != 0:
#     print(f'\n{cores["ciano"]}CALCULADORA DE FATORIAL{cores["reset"]}\n') 
#     n = int(input('Informe o numero desejado: \n'))
#     print(f'O resultado do FATORIAL é {cores["verde"]}{factorial(n)} {cores["reset"]}\n')
#     print(f'Se Desejar sair digite {cores["vermelho"]}0{cores["reset"]}\n\n')

# Sem 
while n != 0:
    print(f'\n{cores["ciano"]}CALCULADORA DE FATORIAL{cores["reset"]}\n') 
    n = int(input('Informe o numero desejado: \n'))
    resul = n
    for i in range(1,n):
        resul *= (n-i)
    print(f'O resultado do FATORIAL é {cores["verde"]}{resul} {cores["reset"]}\n')
    print(f'Se Desejar sair digite {cores["vermelho"]}0{cores["reset"]}\n\n')