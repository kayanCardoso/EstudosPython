# Analisando nome

nome = input('Informe seu nome : ')
n2 = nome.split()
print(f'Seu nome em letras maiúsculas {nome.upper()}')
print(f'seu nome em letras minúsculas {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras !!')
print(f'Seu primeiro nome é {n2[0]} e tem {len(n2[0])} letras !!')
