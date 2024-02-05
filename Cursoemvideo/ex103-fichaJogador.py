
def ficha(nome='',gols=0):
    if nome == '' and gols == 0:
        return 'O jogador <DESCONHECIDO> fez 0 gol(s)'
    elif nome == '' and gols > 0:
        return f'O jogador <DESCONHECIDO> fez {gols} gol(s)'
    else:
        return f'O jogador {nome} fez {gols} gol(s)'
    
nome = input('informe o nome: ')
gols = input('Informe os gols:')
if gols != '':
    gol = int(gols)
    while gol < 0:
        gols = int(input('É impossivel o jogador ter saldo negativo!! Informe corretamente: '))
        gol = int(gols)
    print(ficha(nome,gol))
else:
    print(ficha(nome))
