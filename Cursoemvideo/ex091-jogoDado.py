from random import randint
from time import sleep
from operator import itemgetter
s =1
input()
jogador = {
    'jogador 1': randint(0,6),
    'Jogador 2': randint(0,6),
    'Jogador 3': randint(0,6),
    'Jogador 4': randint(0,6)
}
ranking = list()
sleep(0.5)
for k, v in jogador.items():
    print(f'o {k} tirou {v}')
    sleep(0.5)
print('{:^30}'.format('RESULTADO'))
for i in sorted(jogador, key=jogador.get, reverse=True):
    print(f'{s}° lugar: {i} com {jogador[i]}')
    sleep(0.5)
    s += 1 

# resolução guanabara 👇
    
ranking = sorted(jogador.items(), key=itemgetter(1),reverse=True)
print('~='*10)
for i, v in enumerate(ranking):
    print(f'O {i+1}° foi {ranking[i][0]} com {ranking[i][1]}')

