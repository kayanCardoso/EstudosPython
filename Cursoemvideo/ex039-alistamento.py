from datetime import date
nascimento = int(input('Qual ano você naceu ?\n'))
ano = date.today().year
if (ano - nascimento ) > 17:
    print(f'Você passou do tempo de alistamento, seu \033[31mATRASO\033[m é de {(ano - nascimento) - 17} anos !!')
elif (ano - nascimento) == 17:
    print('Você está na idade de se alistar !! ')
else:
    print(f'Você ainda não está na idade de se alisatar \033[31mFALTAM {17-(ano - nascimento )}\033[m anos')