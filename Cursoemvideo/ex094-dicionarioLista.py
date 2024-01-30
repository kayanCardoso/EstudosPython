pessoas = list()
acima = list()
info = dict()
media = 0 
while True:
    info['nome'] = input('Informe o nome: ').capitalize()
    sex = str(input('Informe o sexo[M/F]: ')).upper().strip()[0]
    while sex not in 'MF':
        sex = input('Informe uma opção valida[M/F]').upper().strip()[0]
    info['sexo'] = sex 
    info['idade'] = int(input('Informe a idade :'))
    media += info['idade']
    saida = input('Deseja continuar [S/N]: ').upper().strip()[0]
    while saida not in 'SN':
        saida = input('Informe uma opção valída[S/N]: ').upper().strip()[0]
    pessoas.append(info.copy())
    if saida == 'N':
        break

print(media)
print('~='*25)
print(f'O grupo tem {len(pessoas)} pessoas.')
print(f'A media de idade é {media / len(pessoas):.2f}')
print(f'As mulheres cadastradas foram: ',end=' ')
for i,v in enumerate(pessoas):
    if pessoas[i]["sexo"] == 'F':
        print(pessoas[i]["nome"], end=' ')
print(f'\nLista das pessoas acima da medía:\n')
for i,v in enumerate(pessoas):
    if pessoas[i]["idade"] > (media / len(pessoas)):
        acima.append(pessoas[i])
for i, v in enumerate(acima):
    print(f'nome = {acima[i]["nome"]}, sexo = {acima[i]["sexo"]}, idade = {acima[i]["idade"]}\n')

