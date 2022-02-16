##Ejercicio 1
# Declaramos 2 variables

new_planet = ''
planets = []

# Ciclo while

while new_planet.lower() != 'hecho':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Ingresa un nuevo planeta ')
##Ejercicio 2
# Ciclofor

for planeta in planets:
    print(planeta)

