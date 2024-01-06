frase = str(input('Informe a frase :\n')).replace(' ','').lower()
tam = int(len(frase))
fr = []
frv = []
for i in range(0,tam):
    print(frase[0:i])
    fr = frase[:tam]
for i in range(0,tam):
    frv = frase[tam:i]
print(fr,frv)