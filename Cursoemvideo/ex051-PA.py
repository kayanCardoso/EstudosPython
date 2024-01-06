p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
for i in range(0,10):
    print(f'A progressão é de {p}')
    p += (p + r) - p