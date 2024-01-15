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

print(f'{cores["vermelho"]}MINI CALCULADORA{cores["reset"]}')
x = int(input('Informe o primeiro valor: '))
y = int (input('Informe o segundo valor: '))
print(f'{cores["amarelo"]}[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]PARA SAIR{cores["reset"]}')
c =  int(input('Informe a opção: '))
while c != 5: 
    if c == 1:
        print(f'O resultado da soma de {x} + {y} é {x+y}\n')
    elif c == 2:
        print(f'A Multiplicação de {x} * {y} é {x*y}\n')
    elif c == 3:
        if x > y:
            print(f'O maior número é {x}\n')
        else:
            print(f'O maior número é {cores["vermelho"]}{y}{cores["reset"]}\n')
    elif c == 4:
        print('Informe os novos numeros ')
        x = int(input('Primeiro: '))
        y = int(input('Segundo: \n'))
    elif c > 5:
        print('Opção invalida !!!')
    print('~'*20)
    print(f'{cores["amarelo"]}[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n{cores["reset"]}')
    c =  int(input('Informe novamente a opção:\n'))
print('saiu')