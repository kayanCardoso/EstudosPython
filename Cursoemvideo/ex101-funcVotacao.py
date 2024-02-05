def voto(n):
    from datetime import date
    x = date.today().year
    if x - n >=18:
        return f'Você tem {x-n} anos o voto é obrigatorio !!!'
    elif x-n >=16 :
        return f'Você tem {x-n} anos o voto é opcional !!'
    else:
        return f'Você tem {x-n} anos não pode votar !!!'
    
idade = int(input('Informe sua data de nascimento: '))
while idade >= 2024 or idade <= 1920:
    idade = int(input('você não tem essa idade informe corretamente: '))

print(voto(idade))

