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

tot = contMais1000 =  0
menor = 9999999999999
nomeMaisBarato = ''

while True:
    print(f'{cores["roxo"]}LOJINHA\n {cores["reset"]}')
    nome = str(input('Nome do produto? ')).strip().capitalize()
    preco = float(input('Qual preço: R$'))
    while preco < 0 :
        preco = int(input('Qual preço: R$'))
    tot += preco
    if preco > 1000:
        contMais1000 += 1
    if preco < menor:
        menor = preco
        nomeMaisBarato = nome
    sair = str(input('Deseja continuar? [S/N]')).upper().strip()
    while sair not in 'SN':
        sair = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break
print(f'{cores["verde"]}O total gasto na compra foi de RS{tot:.2f}')
if contMais1000 == 1:
    print('Um produto custou mais de R$1000')
else:
    print(f'{contMais1000} produtos custaram mais de R$1000')
print(f'O produto mais barato foi {nomeMaisBarato} e custou R${menor:.2f}{cores["reset"]}')