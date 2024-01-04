from datetime import date, datetime

nasc = int(input('Informe seu ano de nascimento:\n'))
ano = date.today().year
categ = ano - nasc

if categ <= 9:
    print('Sua categoria é MIRIM!!!')
elif categ <= 14: 
    print('Sua categoria é INFANTIL!!!')
elif categ <= 19:
    print('Sua categoria e JUNIOR!!!')
elif categ <= 20:
    print("Sua categoria é SENIOR!!!")
else:
    print('Sua categoria é MASTER!!!')