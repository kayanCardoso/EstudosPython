frase = str(input('Informe a frase :\n')).replace(' ','').lower()
tam = len(frase)
inverso = ''
print(frase)
for i in range(tam -1 ,-1,-1):
    inverso += frase[i]

if inverso == frase:
    print(f'{frase} é igual ao seu inverso {inverso}, por isso é um \033[31mPALÍNDROMO!!!\033[m')
else:
    print(f'{frase} não é igual ao seu inverso {inverso}, por isso não é um \033[31mPALÍNDROMO!!!\033[m')