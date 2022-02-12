## EJERCICIO 1
#1 Añade el código necesario divide el texto en cada oración para trabajar con su contenido:
#2 Define las palabras pista: average, temperature y distance suenan bien
#3 define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
from typing import Text

#1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate"""
text2=text.split('. ')
text2

palabracable= ["average", "temperature", "distance"]
#2
for frase in text2:
    for palabra in palabracable:
        if palabra in frase:
            print(frase)
            break

#3
for frase in text2:
    for palabra in palabracable:
        if palabra in frase:
            print(frase.replace(' C', ' Celsius'))
            break

##Ejercicio 2
# 1Datos con los que vas a trabajar
# 2Creamos el título
# 3Creamos la plantilla
# 4Unión de ambas cadenas
#1
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"
#2
titulo=f'\ndatos de gravedad'
#3
preplantilla=f"""\nnombre: {name} \ngravedad:{gravity*1000} m/s2 \nplaneta: {planet} """
#4
plantilla = f"""{titulo.title()} {preplantilla} """ 
print(plantilla)
#5 Nueva luna 
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
otraplanti=new_template = """
Datos de Gravedad
Nombre: {nombre}
Gravedad: {gravedad} m/s2
Planeta: {planeta}
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))


