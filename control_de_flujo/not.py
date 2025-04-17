#Diego Rojas
#02/04/25
#tengo mas hambre que la cresta

respuesta = input ('Estas cansado? (si / no):').strip().lower()

cansado = respuesta == 'si'

if not cansado:
    print('Es hora de programar')

else:
    print('Tomate un descanso, lo necesitas')