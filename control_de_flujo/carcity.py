#Diego Rojas
#Estoy enfermo y cansado

altura = int(input('Cual es tu altura? (cm)'))
#se escribion variables para solicitar información del alumno
creditos = int(input('Cuantos creditos tienes?'))

if altura >= 137 and creditos  >=10:
    print('Disfruta eñ viaje madafaka')

elif altura <=137 and creditos >=10:
    print('No tienes la altura suficiente para subir')

elif creditos <=10 and altura >=137:
    print('No tienes los creditos suficientes')

else:
    print('Cagaste XD')