peso = float(input('Informe seu peso :\n'))
altura = float(input('Informe sua altura;\n'))
imc = peso / altura ** 2 

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}, você está abaixo do peso!!!')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f}, você está no peso ideal!!!')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f}, você está com sobrepeso!!!')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f}, você está com obesidade!!!')
else: 
    print(f'Seu IMC é de {imc:.2f}, você está com obesidade morbida!!!')