#Ejercico 1

# Creamos la lista planets y la mostramos
planets=["Venus","Mercurio","Jupiter","Saturno","Tierra","Marte","Urano","Neptuno"]
print("Los planetas son: ",planets)
# Agregamos a plutón y mostramos el último elemento
planets.append("Pluton")
print(planets[8])

#Ejercicio 2
# Lista de planetas
planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
# Solicitamos el nombre de un planeta 
nomplanet=input("Ingresa el nombre de un planeta, recuera que la primera letras es en mayusculas")
# Busca el planeta en la lista
planeta_index = planetas.index(nomplanet)
# Muestra los planetas más cercanos al sol
print('Los planetas mas cercanos en direccion al sol de',nomplanet, " son:")
print(planetas[0:planeta_index])
print('Los planetas mas aljeados en direccion al sol de ',nomplanet, " son:")
print(planetas[planeta_index + 1 :])
