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
soma = contador = maior = menor = media = 0
while c != 0 :
    numeros = int(input('Informe os números desejados: '))
    contador += 1
    if contador == 1:
        menor = numeros
    if maior < numeros:
        maior = numeros
    if menor > numeros :
        menor = numeros
    soma += numeros
    media = soma / contador
    if contador >= 3:
        print('Deseja ver os resultados ?')
        s = int(input('\n[1]SIM\n[2]NÃO\n'))
        if s == 1:
            print(f'O maior número foi {cores["vermelho"]}{maior}{cores["reset"]}, o menor {cores["vermelho"]}{menor}{cores["reset"]} e a média foi {cores["vermelho"]}{media:.2f} {cores["reset"]} !!!')
    if contador >= 3:
        c = int(input(f'Deseja continuar ?\n{cores["roxo"]}[1]SIM\n[0]NÃO\n {cores["reset"]}'))