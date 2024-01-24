tot = 1
nums = list()
nums.append(int(input('Digite o valor desejado: ')))
while True:
    c = str(input('Deseja continuar[S/N]')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('Informe uma opção valída!! [S/N]')).strip().upper()[0]
    if c == 'S':
        nums.append(int(input('Digite o valor desejado: ')))
        tot += 1
    else:
        break
print(f'Foi digitado {tot} valores !!')
if 5 in nums:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista !!')
nums.sort(reverse=True)
print(f'A lista no formato decrescente{nums}')
