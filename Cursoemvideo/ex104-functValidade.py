def leiaint(text):
    while True:
        n = input(text).strip()
        if n == '' or n == ' ':
            n = 'a'
        y = 0
        pode = True
        while y <= len(n):
            if ord(n[0]) < 48 or ord(n[0]) > 57:
                pode = False
                y+=1
            else:
                y+=1
        if pode == False:
            print('Erro!! Informe um número inteiro ')
        else:
            break
    n1 = int(n[0])
    return f'Você digitou o número {n1}'

print(leiaint('Digite um número: '))
