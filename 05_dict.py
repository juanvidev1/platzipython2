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