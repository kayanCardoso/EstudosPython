# Mostrando informaçoes do texto escrito
msg = input('Digite algo : ')

print('O tipo primitivo desse valor é ', type(msg))
print('Só tem espaços ?', msg.isspace())
print('É um número ?', msg.isnumeric())
print('É alfanumerio ? ', msg.isalnum())
print('É Alfabatico ? ', msg.isalpha())
print('Está em maíuscula ? ', msg.isupper())
print('Está em minúsculo ? ', msg.islower())
print('Está captalizado ? ', msg.istitle())

