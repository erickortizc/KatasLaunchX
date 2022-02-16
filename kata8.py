##Ejercicio 1
# Diccionario planetas
planet = {
    'name': 'Mars',
    'moons': 2
}

# mostrar los planetas y lunas
print(f'{planet["name"]} has {planet["moons"]} moons')


# Agregando circunferencias 
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
 #Imprime el nombre del planeta con su circunferencia polar.
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

## Ejercicio 2
# Añade el código para determinar el número de lunas.
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
# Obtenemos la lista de las lunas
# Almacenamos los resultados en una variable moons
moons = planet_moons.values()

# Obtenemos el total de planetas
# Almacenamos los resultados en una variable llamada years
planets = len(planet_moons.keys())
# Calcula el total_moons agregando todas las lunas
# Almacena su valor en una variable llamada total_moons

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

# Calcula el promedio dividiendo el total_moons por el número de planetas
average = total_moons / planets

# Muestra el promedio
print(average)

