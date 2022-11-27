
# Para obtener el apto en la actividad será necesario entregar el código y una captura de pantalla del programa en funcionamiento.

# 1. Programa de cálculo de edad y saludo:

#     Pedimos los datos al usuario en bucle, que pulsará "" (cadena vacía para salir del bucle)
#     Pedimos al usuario nos facilite su nombre y la edad
#     Guardamos los datos en 2 variables
#     Calculamos el año de nacimiento que guardaremos en otra variable
#     Mostramos los 3 datos en pantalla

import datetime;

while True :
    valor = input('¿Cómo te llamas?(intro para salir)');
    if valor == '':
        break;
    else: nombre = valor;
    valor = input('¿Qué edad tienes?: (intro para salir)');
    if valor == '':
        break;
    else: edad = valor;

if edad!= '':
    date = datetime.date.today()
    annoActual = date.strftime("%Y");
    annoNacimiento = int(annoActual) - int(edad);
    print(str(nombre) + ', tu edad es '+ edad + ' y tu año de nacimiento es '+ str(annoNacimiento));