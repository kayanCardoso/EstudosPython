matriz =[[],[],[]]
somaP = soma3 = maior =0
for i,c in enumerate(matriz):
    for c in range(0,3):
        matriz[i].append(int(input(f'Informe o número desejado na posição [{i},{c}]: ')))
        if matriz[i][c] % 2 == 0:
            somaP += matriz[i][c]
for i,c in enumerate(matriz):
    soma3 += matriz[i][2]
for c in range(0,3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
        
print(f'A soma dos valores pares é {somaP}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')
