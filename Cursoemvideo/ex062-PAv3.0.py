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
contador = 10 
p = int(input('Informe o primeiro termo: '))
aux = p
r = int(input('Informe a razão: '))
while n != 0:
    for i in range(0,contador):
        if i == 0:
            print('A progressão é de ', end='')
        print(p, end=' ')
        p += (p + r) - p
        
    n = int(input(f'\n{cores["vermelho"]}Deseja saber mais progressoes ?{cores["reset"]}\n0-NÃO\nINFORME O VALOR DESEJADO: ')) 
    if n >= 1:
        contador = 0
        contador += (10+n)
        p = aux
    elif n < 0: 
        print('OPÇÃO INVALIDA-O programa será fechado')
        n = 0
