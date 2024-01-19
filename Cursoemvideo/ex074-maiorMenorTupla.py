from random import randint 

num = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
for c in range(0,len(num)):
    if c == 0 : 
        print(f'Os valores sorteados foram {num[c]}', end=' ')
    else:
        print(num[c], end=' ')
print(f'\nO maior número foi {sorted(num)[-1]}')
print(f'e o menor foi {sorted(num)[0]}')