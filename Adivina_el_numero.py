import random

intentos=0

print('¡Hola! ¿Cuál es tu nombre?')
nombre = input()

numero=random.randint(1,20)
print('Bueno, '+nombre+', piensa un número entre 1 y 20.')

while intentos<6:
    print ('¡Adivínalo! Tienes 6 intentos')
    adivina=input()
    adivina=int(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡Muy bajo!')

    if adivina>numero:
        print('¡Muy Alto!')

    if adivina==numero:
        break

if adivina==numero:
    intentos=str(intentos)
    print('¡Súper!, '+nombre+', acertaste el número en '+intentos+' intentos.')

if adivina!=numero:
    numero=str(numero)
    print('¡Qué mal '+nombre+' ! Yo pensé en el número '+numero)