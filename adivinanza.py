#Diego Rojas
#07/04/25
#falto mi pololita y la extraño muchote

adivinanzas = 0
intentos = 0 

while adivinanzas != 0 and intentos > 5:
    adivinanzas = int(input('Adivina el numero: '))
    intentos +=1
if adivinanzas !=6:
    print('Te quedaste sin intentos')
else:
    print('Adivinaste')