num = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: '))
par = 0
if num.count(9)== 1:
    print(f'O número 9 apareceu uma vez')
elif num.count(9) == 0:
    print(f'O número 9 não apareceu nenhuma vez')
else:
    print(f'O número 9 apareceu {num.count(9)} vezes')
if num.count(3) >= 1:
    print(f'O primeiro três foi digitado na posiçao {num.index(3)+1}')
else:
    print('A tupla não teve nenhum número 3 !!')
for c in range(0,len(num)):
    if num[c] % 2 == 0:
        par += 1
if par == 1:
    print('Na tupla teve um número par !!')
else:
    print(f'A tupla teve {par} números pares !!')
 