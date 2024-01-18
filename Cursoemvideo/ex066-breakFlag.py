quant = soma = 0

while True:
    n = int(input('Digite um número(Obs: Digite 999 para sair): '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'A soma dos {quant} valores foi de {soma}')