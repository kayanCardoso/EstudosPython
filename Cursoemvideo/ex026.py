# Procurando o "A"
frase = input('Digite uma frase : ').lower(). strip()
print(f'A letra "a" apareceu {frase.count("a")}')
print(f'A primeira letra "a" apareceu na posição {frase.find("a")+1}')
print(f'A ultima letra "a" apareceu na posição {frase.rfind("a")+1}')
print(len(frase))