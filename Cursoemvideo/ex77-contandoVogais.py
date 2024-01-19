frutas = "abacaxi", "banana", "caqui", "damasco", "embauba", "eiguo", "graviola"
for c in range(0,len(frutas)):
    fatiado = list(frutas[c])
    print(f'Na palavra {frutas[c]} temos as vogais', end=' ')
    for i in range(0,len(fatiado)):
        asc = ord(fatiado[i])
        if asc == 97:
            print('a', end=' ')
        elif asc == 101:
            print('e', end=' ')
        elif asc == 105:
            print('i',end=' ')
        elif asc == 111:
            print('o', end=' ')
        elif asc == 117:
            print('u', end=' ')
    print('\n_________________________________________')
