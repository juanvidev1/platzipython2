"""
EN - The filter function works similary to map, but this just filters the elements of a list into a new one that
contains the elements that fills the condition setted in the function passed as an argument of filter function.
It's declared like this:
    filtered_items = list(filter(lambda x: <expected return> <condition to be filled>, <iterable item>))

Don't forget that filter generates a NEW LIST just like map

ES - La función filter funciona de manera similar a map, pero esta sólo filtra los elementos de una lista en una
nueva con los elementos que cumplan con una condición establecida en la función pasada como un argumento de la
función filter.
Se declara así:
    filtered_items = list(filter(lambda x: <retorno esperado> <condición a cumplir>, <elemento iterable>))

No olvidar que filter genera una NUEVA LISTA tal como lo hace map
"""

numbers = [i for i in range(1, 6)] # Generates an example list

print(numbers)

new_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Obtains the even numbers and stores them in the new_numbers list
print(new_numbers)

"""
EN - We can also use filter with dictionaries lists. Just like we did with map function

ES - También podemos utilizar filter con listas de diccionarios. Tal como los hicimos con la función de map.
"""

