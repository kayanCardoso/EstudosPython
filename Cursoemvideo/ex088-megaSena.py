
from random import sample
from time import sleep

print('-'*30)
print('MEGA SENA'.center(30))
print('{:^30}'.format('MEGA SENA'))
print('-'*30)
jogos = list()
aux = list()
n = int(input('Quantos jogos você deseja ? '))
for c in range(0,n):
    jogos.append(sample(range(1, 60), 6))
    jogos[c].sort()
print('=~'*30)
print('{:^30}'.format('RESULTADOS'))
sleep(1)
for c in range(0,n):
    print(f'{c+1}°: {jogos[c]}')
    sleep(0.5)
