matriz = [[],[],[]]
for i,c in enumerate(matriz):
    for c in range(0,3):
        matriz[i].append(int(input(f'Informe o número desejado na posição [{i},{c}]: ')))
for i,c in enumerate(matriz):
    print(f'[ {matriz[i][0]:^5} ] [ {matriz[i][1]:^5} ] [ {matriz[i][2]:^5} ]')

