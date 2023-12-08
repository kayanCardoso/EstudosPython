# Primeiro e ultimo nome

nome = input('Informe seu nome completo : ').capitalize()
n2 = nome.split()
print(f'Seu primeiro nome é {n2[0]}')
print(f'Seu ultimo nome é {n2[-1]}')