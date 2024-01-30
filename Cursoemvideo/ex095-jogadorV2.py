time = list()
jogador = dict()
gols = list()

while True:
    tot = 0
    jogador['nome'] = input('Nome do jogador : ').capitalize()
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou ? '))
    for i in range(1,jogos+1):
        gols.append(int(input(f'Quantos gols na partida {i}: ')))
    for i , v in enumerate(gols):
        tot += gols[i]
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    gols.clear()
    time.append(jogador.copy())
    saida = input('Deseja continuar [S/N]').upper()
    while saida not in 'SN':
        saida = input('Deseja continuar [S/N]').upper()
    if saida == 'N':
        break
print('~='*20)
print('{:5}'.format('COD'),'{:15}'.format('NOME'),'{:12}'.format('gols'),'TOTAL')
print('-'*40)
for i, v in enumerate(time):
    print(f'{i:<5}', f'{time[i]["nome"]:15}', f'{time[i]["gols"]}',f'{time[i]["total"]:>10}')

x = 0
while x != 999:
    x = int(input('Deseja ver os dados de qual jogador(999 saída): '))
    if x > (len(time)-1) or x <= -1:
        if x == 999:
            break
        print(f'O numero {x} é invalido!!!')
    else:
        print(f'\n{time[x]["nome"]}')
        for i, v in enumerate(time):
            print(f'    no {i+1}° jogo fez {time[x]["gols"][i]} gols ')
