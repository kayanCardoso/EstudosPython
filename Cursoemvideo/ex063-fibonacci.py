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

c = 1 
while c != 0:
    print(f'{cores["roxo"]}~'*23)
    print('Sequência de fibonacci')
    print(f'~'*23,f'{cores["reset"]}')
    n = int(input('\nInforme o numero desejado: '))
    aux = 1
    aux1 = 1
    aux2 = 0
    for i in range(0,n):
        if i == 0: 
            print(aux2, end=' ')
            aux2 = 1
        if i < 2:
            aux2 = 1
            aux = 1 
            print(aux2, end=' ')
        else:
            aux2 = aux1 + aux
            aux = aux1
            aux1 = aux2
            print(aux2, end=' ')
    c = int(input('\nPara sair digite "0"\nPara continuar aperte QUALQUER NÚMERO: '))