n = int(input('informe o numero: '))
r = 0
for i in range(2,11):
    if n == i:
        r = r
    else:
        if n % i == 0:
            r = 1
if r == 1:
    print(f'O número {n} não é \033[32mPRIMO!!!\033[m')
else:
    print(f'O numero {n} é \033[32mPRIMO!!!\033[m')