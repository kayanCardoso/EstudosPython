nums = list()
par = list()
impar = list()
nums.append(int(input('Digite o valor desejado: ')))
while True:
    c = str(input('Deseja continuar[S/N]')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('Informe uma opção valída!! [S/N]')).strip().upper()[0]
    if c == 'S':
        nums.append(int(input('Digite o valor desejado: ')))
    else:
        break
tam = len(nums)
for c in range(0, tam):
    if nums[c] % 2 == 0:
        x = nums[c]
        par.append(nums[c])
    else:
        impar.append(nums[c])
print(f'A lista principal é {nums}')
print(f'A de numeros pares {par}')
print(f'A de números ímpares {impar}')
