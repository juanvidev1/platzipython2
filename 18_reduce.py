"""
EN - The reduce function is a python function that takes a list as an argument and reduces it to a unique value
that is like a conclusion of that list (for example the summatory of al elements of a numeric list). The example
below shows how this works

ES - La función reduce es una función the python que toma una lista como argumento y la reduce a un valor único
que es como la conclusión de esa lista (por ejemplo la sumatoria de todos los elementos de una lista numérica).
El ejemplo de abajo muestra como trabaja esta función
"""

import functools # This import is necessary to use reduce built in function

numbers = [i for i in range(1, 5)]

print(numbers)

def accum(counter, item):
    print('counter => ' + str(counter))
    print('item => ' + str(item))
    return counter + item

result = functools.reduce(accum, numbers)
print(result)