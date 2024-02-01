def escre(msg):
    s = len(msg)
    print('-'*(s+4))
    print(f'  {msg}')
    print('-'*(s+4))


x = input('Informe a mensagem desejada: ')
escre(x)
