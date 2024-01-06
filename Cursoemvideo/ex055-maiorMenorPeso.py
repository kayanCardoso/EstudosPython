maior = 0
menor = 1000
for i in range(0,5):
    peso = float(input('Informe seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O Maior peso é {maior:.1f}KG e o menor é {menor:.1f}KG')