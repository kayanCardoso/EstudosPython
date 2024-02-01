import random

def sorteia(lst):
    x = list()
    x = random.sample(lst, 5)
    return x 

def somapar(a):
    print('-'*30)
    pos = 0
    soma = 0
    while pos < len(a):
        if a[pos] % 2 == 0:
            soma += a[pos]
        pos+=1
    print(f'O resultado da soma dos pares da lista é {soma}')



tropa = list()

while True:
    print('Digite 7 Números')
    for i in range(0,7):
        tropa.append(int(input(f'informe o {i+1}° numero: ')))
    saida = input('Deseja continuar ? [S/N]').upper()[0]
    while saida not in 'SN':
        saida = input('Deseja continuar ? [S/N]').upper()[0]
    if saida == 'N':
        break

sorteados = sorteia(tropa)
print(f'Numeros sorteados {sorteados}')
somapar(sorteados)