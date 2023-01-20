"""
EN - Like the comprehensions on lists, you also can include if conditions inside the dictionary creation. Let's see again the population by country exercise
from the last class created with dictionary comprehension:

ES - Como en las comprehensions en las listas, también se pueden incluir condicionales dentro de la creación del diccionario. Veamos nuevamente el ejercicio de
población por país de la clase pasada creado con dictionary comprehension:
"""
import random
countries = ['Col', 'Mex', 'Bol', 'Pe', 'Arg', 'Bra', 'Uru', 'Ven', 'Chi', 'Par', 'Ecu']
population = {i: random.randint(1, 100) for i in countries}
print(population)

"""
EN - In the example above the value will change because we are generating randonmly the population, but in any case we can generate a conditional for this
this example, where we are going to create a new dictionary with the countries that has at least 50 people of population letting those countries with a pop
below 50 out of the new dict. The following code is the solution for this

ES - En el ejemplo de arriba el valor siempre cambiará porque estamos generando aleatoriamente la población de cada país, pero en todo caso generaremos una 
condición, para este ejemplo, donde se creará un nuevo diccionario con los países que tengan un población de al menos 50 personas, dejando a esos países con
una población por debajo de 50 fuera del nuevo diccionario. El siguiente código es la solución a ese problema
"""
big_countries = {country: population for (country, population) in population.items() if population > 50}
print(big_countries)
"""
EN - In the code above we have the dict comprehension where key:value pairs are country and it's population based on the population dictionary on line 10.
This pairs are taken from the population dictionary, using it's pair key:value elements, and setted in the new dictionary.
Warning: Don't forget that if you're going to iterate on a dictionary you should iterate it with the .items() method to get correctly the key:value pairs in
each cycle.
Finally we use the conditional, just like we did in lists, to obtain the values that fit the condition statement

ES - En el código anterior tenemos la comprehension de diccionarios donde los pares llave:valor son el país y su población, tomando como base el diccionario
de población que obtuvimos en la línea 10. Estos pares llave:valor se toman de dicho diccionario de población utilizando los pares que contiene el mismo.
Advertencia: No olvidar que si van a iterar sobre el diccionario de población de la línea 10, se debe hacer con el método .items() para obtener correctamente
los pares llave:valor y no tener errores en la iteración
Finalmente utilizamos el condicional, tal como lo hicimos con las listas, para obetener los valores de población que se ajusten a la condición establecida. 
"""