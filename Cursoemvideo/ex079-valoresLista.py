lista = list()
lista.append(int(input('Digite o valor : ')))
while True:
    continuar = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite uma opção valída [S/N]')).strip().upper()[0]
    if continuar == 'S':
            lista.append(int(input('Digite o valor : ')))
            ultimo = lista[-1]
            if lista.count(ultimo) > 1:
                 print('O número já foi adicionado!!!')
                 lista.pop()
    else:
         break
lista.sort()
tam = len(lista)
for c in range(0, tam):
    if c == 0:
        print(f'Você digitou os valores {lista[c]}', end=' ')
    else:
        print(lista[c], end=' ')
