## Ejercicio 1
# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
velocida=49
if velocida > 25:
    print("Cuidado un asteoride se viene acercado  ")
else :
     print("Sin detecciones  ")


##Ejercicio 2
velo=19
if velo >20:
    print("Un asteoride a mas 20 km p h")
elif velo ==20:
    print("Un astoroide a 20 km p h")
else :
    print("No existen astorides")

##Ejercicio 3
##
tamano=40
if tamano >25 and velocida>25 :
    print("Alerta, astoroide muy grande y veloz")
elif velocida ==20:
    print("Un astoroide a 20 km p h")
elif tamano <25:
    print("Sin peligro")
else :
    print("No existen astorides")
