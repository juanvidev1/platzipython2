"""
EN - map() --> Is a python function that transforms the elements inside a given list that contains those elements.
For example if I have the  following animal list:
    groseries = ['cow', 'chicken', 'corn', 'potato']
I can use the map method to transform those elements trought another function, in this example we will be using
the function cook() and when I use map to transform the elements in the animals list I will get a list with the
same 4 elements, but transformed by the logic of the function, in this example an output could be
    groseries_transformed : ['hamburger', 'fried chicken', 'corn pop', 'french fries']
Where the cook function transformed the groseries into food made from those elements from the groseries list
It's important to note that if the original list has 4 elements, the transformed list will have the same number
of elements

ES - map() --> Es una función de python que transforma elementos dentro de una lista dada que contenga esos
elementos. POr ejemplo si tengo la siguiente lista:
    viveres = ['vaca', 'pollo', 'maíz', 'papa']
Puedo utilizar el método map para transformar esos elementos, a través de una función. En este ejemplo usaremos
la función cocinar() y cuando utilice map para transformar los elementos de la lista de víveres a través de la
función cocinar obtendré una lista de los mismos elementos, pero transformados por la lógica de la función, en 
este ejemplo una salida podría ser
    viveres_transformados = ['hamburguesa', 'pollo asado', 'palomitas de maíz', 'papas fritas']
Donde la función cocinar transformó los víveres en comida hecha a partir de los elementos de la lista de víveres
Es importante anotar que si la lista original tiene 4 elementos, la lista transformada tendrá el mismo número de
elementos que la lista original
"""
# Here we create a simple number list using dict comprehension
numbers = [element for element in range(1, 11)]
print(numbers)

# Here we transform the simple number list using dict comprehension
numbers_v2 = [number * 2 for number in numbers]
print(numbers_v2)

# Here we transformed the simple number list using lambda functions and the map method
numbers_v3 = list(map(lambda i : i * 2, numbers)) # The map method receives a function argument and a list argument --> The function will perform the transformation of the elements, the list argument contains the elements to be converted
print(numbers_v3)