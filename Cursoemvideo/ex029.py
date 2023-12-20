# Velocidade maxima

vel = int(input('Qual velocidade atual do veiculo ?\n'))
if vel > 80:
    print('você ultrapassou a velocidade limite de 80km!!')
    print(f'Sua multa é de R${(vel-80)*7:.2f}')
else:
    print('Você está com velocidade dentro do limite!!')