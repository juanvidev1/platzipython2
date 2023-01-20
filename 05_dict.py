"""
EN - The same comprehension that is used for lists can be used for dictionaries. Normally we used a for cycle for extract "key":"value" elements from a dictionary
but this can be done the same way that we did with lists. The normal way to do this is the following:
dict = {}
for i in range(1, 11):
    dict[i] = i --> The [i] is the "key" of the "key":"value" pair in the dictionary (don't forget that the python dictionaries must have a key:value pairs inside)
print(dict)
The following exercise shows how to do this with dictionary comprehension

ES - La misma comprehension que utilizamos con las listas funciona con los diccionarios. Normalmente usamos un ciclo for para extraer un 
par "llave":"valor" de un diccionario, pero esto puede hacerse de la misma manera que lo hicimos con el list comprehension. La manera normal es la siguiente:
for i in range(1, 11):
    dict[i] = i --> La [i] será la llave del par "llave":"valor" en el diccionario (no olvidar que los diccionarios en python deben contener pares llave:valor)
print(dict)
El siguiente ejercicio muestra la salida del ciclo normal y luego la forma de hacerlo con dictionary comprehension 
"""
dict = {}
for i in range(1, 11):
    dict[i] = i  

print(dict)

"""
EN - Now the way to do it in one line with dictionary comprehension

ES - Ahora la manera de hacerlo en una línea con dictionary comprehension
"""
dict_v2 = {i:i for i in range(1, 11)}
print(dict_v2)

import random ;"EN - Here we import the random library to generate a dynamic population number // Importamos esta librería para generar un número aleatorio para la población"
countries = ['Col', 'Mex', 'Bol', 'Pe', 'Arg', 'Bra', 'Uru', 'Ven', 'Chi', 'Par', 'Ecu']
"""
EN - We can also create dictionaries from other data structures, like lists. For example a countries list, that we have above, can generate a dictionary
wich will have a country name and it's population. 
There are 2 ways of doing this:
    1. The whole life way using a for cycle, creating an empty dictionary and inside the for adding the pair key:value to the dict. The code will be the following.
    Warning: It's important to create de dictionary before iterate on the for cycle:
    population = {}
    for i in countries:
        population[i] = random.randomint(1, 100) --> You can copy and paste this three lines of code outside the comments to see how it works
    
    2. The dictionary comprehension method wich we will see in the example below:

ES - También podemos crear diccionarios de otras estructuras de datos, como las listas. Por ejemplo una lista de países, que ya tenemos antes de este comentario,
podemos generar un diccionario que tendrá el nombre de un país y su población.
Hay dos formas de hacer esto:
    1. La forma de toda la vida utilizando un ciclo for, declarando previamente un diccionario vacío para, dentro del for, agregar el par key:value al diccionario
    El código sería el siguiente:
    Advertencia: Es importante declarar el diccionario vacío antes de iterar en el ciclo
    population = {}
    for i in countries:
        population[i] = random.randomint(1, 100) --> Puedes copiar y pegar este código fuera de los comentarios para poder ver su funcionamiento

    2. Con el método de dictionary comprehension que veremos en el ejemplo de abajo 
"""
population = {i: random.randint(1, 100) for i in countries}
print(population)

names = ['Nico', 'Zule', 'Santi']
ages = [12, 56, 98]
"""
EN - Now we're going to try to iterate 2 lists, that we have above (names and ages), and generate a dictionary taking those list to obtain the pair 
key:value from both lists (key from names and value from ages). The way to do this is the following:
    - You should join the 2 lists. You can do this using the method zip in this way:
        zip(names, ages) --> If you print this you won't have really a list, will obtain a reference that the lists were joined, but not the data. 
        Must convert it to a list like this if you want to see it's content (but this is not necessary for create de dictionary):
        list(zip(names, ages)) --> The output of this will be a tuples list (the examples below shows this better everything is written here)
    
ES - Ahora vamos a tratar de de iterar 2 listas, que ya tenemos arriba de este comentario (names y ages), y generar un diccionario tomando esas listas
para obtener los pares llave:valor de ambas listas (llave de la lista names y valor de la lista ages). La manera de hgacer esto es la siguiente:
    - Debes unir las dos listas. Esto se puede hacer utilizando el método zip de esta forma:
        zip(names, ages) --> Esto devuelve una referencia indicando el zip object que fusionó las dos listas. Es con el que trabajamos
        list(zip(names, ages)) --> Esto devuelve una lista de tuplas, para entender mejor qué contiene el objeto zip con el que trabajaremos (el ejemplo de
        abajo muestra mejor todo lo que está escrito aquí)
"""
new_dict = {name:age for (name, age) in zip(names, ages)}
print(new_dict)