"""
EN - A set is a data element wich allows to add dara from any kind inside of it. An interesting thing about the sets it's that this data structure 
delete all duplicated elements inside it. Surely it will let you create your set with duplicated elements, but when you will be using it, the duplicates 
will not exist. Other interesting thing is that the print of a set will be randon, the elements will print in different order everytime in case of sets of strings

ES - Un conjunto es un elemento que permite agrupar datos de distintos tipos dentro de si. Una cosa interesante es que no permite los elementos 
duplicados se eliminan automáticamente de un conjunto. Cuando crees el conjunto con elementos duplicados, no te va poner problema, 
pero cuando vayas a utilizar la data de ese conjunto, los elementos duplicados, ya no existirán. Otra cosa interesante en que cada print de un conjunto,
el orden de los elementos va a ser diferente cada vez cuando son strings 
"""

"""
EN - This is one of the ways that a sets can be created: set_name = {element1, element2, element3, ...}
ES - Esta es una de las formas básicas de definir un conjunto: nombre_conjunto = {dato1, dato2, dato3, ...}
"""
set_countries = {'Col', 'Mex', 'Bol'}
print(type(set_countries))
print(set_countries)

"""
EN - A set can contain strings, like the example above, or can contain numbers like the following example
ES - Puede ser de strings como en el conjunto anterior o de números como el siguiente ejemplo
"""
set_numbers = {1, 2, 3, 4, 4, 4.5, 5}
print(set_numbers)

"""
EN - A set can contain mixed data too, as you can see in the following example:
ES - El conjunto puede tener elementos de diferentes tipos como en el siguiente ejemplo:
"""
set_types = {1, False, "Hello", 'Hola', 'Hola', 3.8}
print(set_types)

"""
EN - Also you can get a set from another data type, for example a string: set(string_to_be_converted_to_set)
ES - También puedes obtener un conjunto de otro tipo de dato, por ejemplo de un string: set(string_a_convertir)
"""
set_from_string = set('Hola')
print(set_from_string)

"""
EN - Same example from above but with a tuple
ES - El mismo ejemplo anterior, pero con una tupla
"""
set_from_tuple = set(('abc', 'cfg', 'dse', 'abc'))
print(set_from_tuple)

set_numbers_2 = {2, 1, 6, 3, 4, 7, 5}
print(set_numbers_2)

"""
EN - To see this code working you should write the command 'python 01_set.py' on the shell. 
Warning: You must have installed python on your system to execute the code

ES - Para ver este código funcionando debes escribir el comando 'python 01_set.py' en la shell. 
Advertencia: Debes tener instalado python en tu sistema para poder ejecutar el código
"""
