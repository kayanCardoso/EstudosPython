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

from random import randint
venceu = 0
print('=~'*30)
print('Jogo do PAR ou IMPAR')
print('=~'*30)
while True:
    comp = randint(1,10)
    pess = int(input('Informe sua Jogada: '))
    jogada = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
    if jogada == 'I':
        if (comp + pess) % 2 == 1:
            print(f'{cores["ciano"]}Eu Joguei {comp} e você {pess}{cores["reset"]}')
            print('Você VENCEU!')
            print('=~'*30)
            print('Revanche 😡\n')
            venceu += 1
        else:
            print(f'{cores["ciano"]}Eu Joguei {comp} e você {pess}{cores["reset"]}')
            print('Você PERDEU!')
            print('=~'*30)
            print(f'{cores["verde"]}Você venceu {venceu} vezes{cores["reset"]}')
            break
    elif jogada == 'P':
        if (comp + pess) % 2 == 0:
            print(f'{cores["ciano"]}Eu Joguei {comp} e você {pess}{cores["reset"]}')
            print('Você VENCEU!')
            print('=~'*30)
            print('Revanche 😡\n')
            venceu += 1
        else:
            print(f'{cores["ciano"]}Eu Joguei {comp} e você {pess}{cores["reset"]}')
            print('Você PERDEU!\n')
            print('=~'*30)
            print(f'{cores["verde"]}Você venceu {venceu} vezes{cores["reset"]}')
            break
    else:
        print(f'\n{cores["vermelho"]}INFORME UMA OPÇÃO VALÍDA!!!{cores["reset"]}')