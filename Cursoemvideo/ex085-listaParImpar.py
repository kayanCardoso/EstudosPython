valor = [[],[]]

for c in range(0,7):
    n = int(input(f'Digite o {c+1}° valor : '))
    if n % 2 == 0:
        valor[0].append(n)
    else:
        valor[1].append(n)
valor[0].sort()
valor[1].sort()
print(f'Os valores pares {valor[0]}\nOs ímpares {valor[1]}')
