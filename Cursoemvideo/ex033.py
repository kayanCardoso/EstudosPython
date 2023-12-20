'''n1 = int(input('Informe o primeiro numero : '))
n2 = int(input('Informe o segundo numero : '))
n3 = int(input('Informe o terceiro numero : '))
# minha solução
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'O maior numero é {n1}')
        print(f'O menor numero é {n3}')
    else:
        print(f'O maior numero é {n1}')
        print(f'O menor numero é {n2}')
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'O maior numero é {n2}')
        print(f'O menor numero é {n3}')
    else:
        print(f'O maior numero é {n2}')
        print(f'O menor numero é {n1}')
else:
    if n2 > n1:
        print(f'O maior numero é {n3}')
        print(f'O menor numero é {n1}')
    else:
        print(f'O maior numero é {n3}')
        print(f'O menor numero é {n2}')'''

# Solução do Guanabara
a = int(input('Informe o primeiro numero:'))
b = int(input('Informe o primeiro numero:'))
c = int(input('Informe o primeiro numero:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior numero é {maior}')
print(f'O menor numeor é {menor}')













