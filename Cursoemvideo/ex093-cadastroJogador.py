jogador = dict()
gols = list()
tot = 0
jogador['nome'] = input('Nome do jogador : ')
jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou ? '))
for i in range(1,jogos+1):
    gols.append(int(input(f'Quantos gols na partida {i}: ')))
for i , v in enumerate(gols):
    tot += gols[i]
jogador['gols'] = gols[:]
jogador['Total'] = tot
print('~='*20)
print(f'{jogador["nome"]}')
print(f'{jogador["gols"]}')
print(f'{jogador["Total"]}')
print('~='*20)
print(f'O jogador {jogador["nome"]} jogou {len(gols)} jogos.')
for i , v in enumerate(gols):
    print(f'   => Na {i+1}° partida, fez {v} gols')
print(f'Foi um total de {tot} gols.')
