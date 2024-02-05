def fatorial(n, show=False):
    """
    -> Calcula o fatorial
    para n = Número a se calcular
    para show = mostrar o fatorial ou não(Opcional) 
    return = retorna o valor do fatorial 
    
    """
    i = 1
    if show == True:
        print(f'{n}! =', end=' ')
        for c in range(n,0,-1):
            i *= c
            if c == 1 :
                print(f'{c} =', end=' ')
            else:
                print(f'{c} X',end=' ')
        print(i)
    else:
        for c in range(n,0,-1):
            i *= c
        return f'O valor do fatorial é {i}'


# help(fatorial)
x = int(input('Informe o numero desejado : '))
print(fatorial(x))
