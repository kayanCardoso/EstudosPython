num = int(input('Informe um numero inteiro:'))
print('Escolha a base para conversão: ')
op = int(input('1-Binário\n2-Octal\n3-Hexadecimal\n'))
if op < 1 or op > 3:
    print('Informe um numero valído')
elif op == 1:
    print(f'A conveção de {num} para binário é {bin(num)[2:]}')
elif op == 2:
    print(f'A converção de {num} para octal é {oct(num)[2:]}')
else:
    print(f'A corverção de {num} para hexadecimal é {hex(num)[2.]}')

