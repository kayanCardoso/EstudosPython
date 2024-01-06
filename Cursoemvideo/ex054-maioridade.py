from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(0,7):
    idade = int(input('Informe sua data de nascimento: '))
    if (ano-idade) >= 21:
        maior += 1
    else:
        menor += 1
print(f'O numero de pessoas maior de idade é \033[35m{maior}\033[m '
      f'e o numero de menores de idade é \033[35m{menor}\033[m')