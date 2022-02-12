## EJERCICIO 1
#Declarar variables
tierra=149597870 
jupiter=778547200

distancia=abs(tierra-jupiter)
print("La distancia entre la tierra y jupiter es:" ,distancia,"km")
millas=distancia*0.621
print("La distancia entre la tierra y jupiter es: ", millas,"millas")

##EJERCICIO 2
planeta1=input('Introduzca el valor de la distancia del planeta 1')
planeta2=input('Introduzca el valor de la distancia del planeta 2')

planeta1=int(planeta1)
planeta2=int(planeta2)
distancia=abs(planeta1-planeta2)
print("La distancia entre ambos planetas es: " ,distancia,"km")
millas=distancia*0.621
print("La distancia entre ambos planetas es: ", millas,"millas")