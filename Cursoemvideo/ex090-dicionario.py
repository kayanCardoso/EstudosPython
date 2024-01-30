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


aluno = dict()
aluno['nome'] = input('Informe o nome: ')
n = float(input(f'media de {aluno["nome"]}: '))
while n > 10 or n < 0:
     n = float(input(f'media de {aluno["nome"]}: '))
aluno['media'] = n

print(f'A média de {aluno["nome"]} foi {aluno["media"]}')
if aluno['media'] >= 5:
    aluno['situação'] = 'APROVADO'
    print(f'{cores["verde"]}{aluno["situação"]}{cores["reset"]}')
else:
    aluno['situação'] = 'REPROVADO'
    print(f'{cores["vermelho"]}{aluno["situação"]}{cores["reset"]}')
