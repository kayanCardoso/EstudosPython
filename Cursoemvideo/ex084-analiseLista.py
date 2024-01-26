dados = list()
aux = list()
leve = list()
pesado = list()
tot = maior = menor = 0
while True:
    aux.append(input('Informe o nome: ').capitalize())
    aux.append(float(input('Informe o peso: ')))
    if len(dados)==0:
        menor = aux[1]
    dados.append(aux[:])
    aux.clear()
    tot += 1
    prox = input('Deseja coontinuar [S/N]').upper().strip()[0]
    while prox not in 'SN':
        prox = input('Deseja coontinuar [S/N]').upper().strip()[0]
    if prox == 'N':
        break
for i, v in enumerate(dados):
    if dados[i] == 0:
        maior = dados[0][1]
    else:
        if dados[i][1] > maior:
            maior = dados[i][1]
        if menor > dados[i][1]:
            menor = dados[i][1]
for i , c in enumerate(dados):
    if dados[i][1] == maior:
        pesado.append(dados[i][0])
    if dados[i][1] == menor:
        leve.append(dados[i][0])

        
print(f'Foram cadastradas {tot} pessoas ')
print(f'O Maior peso foi {maior} Peso de  {pesado}')
print(f'O Menor peso foi {menor} Peso de  {leve}')

