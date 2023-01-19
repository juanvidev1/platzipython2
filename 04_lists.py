"""
EN - In this lesson we've worked with list comprehensions. Bassically it means that you can generate list with just one line of code.
Sintax: [element for element in <iterable_element>] --> Here the first "element" is the data that we usually select in a normal for cycle. 
It's the same that "i" in the whole life for cycles
The following examples show this better

ES - En esta clase hemos trabajado con list comprehensions. Básicamente significa que podemos crear listas con una sola línea de código.
Sintaxis: [elemento for elemento in <estructura_datos_iterable>] --> Aparentemente el primer "elemento" en este caso sería el que se selecciona 
en un ciclo normal de for. En resumen es la misma variable i de los ciclos for de siempre
El siguiente ejemplo lo muestra mejor
"""

numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)

numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

"""
EN - Another case is when we want to, for example, multiply the selected element (element or i) to obtain a different result. In a normal for cycle it could be
something like this:
numbers = []
for i in range(1, 11)
    numbers.append(i * 2)
print(numbers)
The following example shows how this code could be with list comprehensions

ES - Otro caso es cuando queremos, por ejemplo, manipular el elemento seleccionado (element o i) para obtener un resultado diferente. En un ciclo normal de for
podría ser algo como esto:
numbers = []
for i in range(1, 11)
    numbers.append(i * 2)
print(numbers)
El siguiente ejemplo muestra este código en sintaxis de list comprehensions
"""
numbers = [i * 3 for i in range(1, 5)]
print(numbers)

"""
EN - Other case is when the for includes a conditional. A normal sintax will be:
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)
print(numbers)
The following code shows this, but with list comprehensions

ES - Otro caso es cuando el ciclo for contiene un condicinal. La sintaxis normal sería:
numbers = []
for i in range(1, 101):
    if i % 2 == 0:
        numbers.append(i * 2)
print(numbers)
El siguiente código muestra esto mismo, pero con list comprehensions
"""
numbers = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers)