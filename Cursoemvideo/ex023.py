# Analisando o número

n1 = int(input('Informe o número : '))
n2 = str(n1)
m = n1 // 1000 % 10
c = n1 // 100 % 10
d = n1 // 10 % 10
u = n1 // 1 % 10
# Formato com String
print(f'Unidade: {n2[3]}\nDezena: {n2[2]}\nCentena: {n2[1]}\nMilhar: {n2[0]}')
print('')
# Forma do Guanabara com a matematica
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')