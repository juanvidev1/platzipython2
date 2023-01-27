"""
EN - In this part we will be learning about return inside the functions. This is important when you need to obtain a value from a function and use it later
inside other part of your code. This will allow you to get more complex operations within functions in your code.

ES - En esta parte aprendermos sobre el return dentro de las funciones. Estos es importante cuando quieres obtener un valor de una función y utilizarlo luego
en otras partes de tu código. Esto te va a permitir hacer operaciones más complejas entre funciones en tu código
"""

def sum_with_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

print(sum_with_range(1, 10))

def hello():
    return 'hello'

def composed_hello(name):
    saludo = hello()
    return saludo + name

result = composed_hello('Juanvi')
print(result)

"""
EN - In the last examples you can see how the return works. Look first at the sum_with_range function where we are giving 2 arguments (integer numbers) and
then pass those same arguments to a range function to iterate over that range and obtain the addition of the numbers inside that range. The return is the
value that results of the addition of the number to the actual value each iteration (e.g. range(1, 10) = 1 + 2 + 3 + 4 + 5 ... + 10)

In the second part we're using 2 functions to create a "Hello <name>" function. The first one just return a "hello" and it's called in the same way.
The second one receives a parameter called name and when we pass the argument (some string instead of var name) it is concatenated to the result of the call
of the hello function saved inside a variable (see line 21).

ES - En los dos ejemplos anteriores puedes ver cómo funciona el return. Primero mira la función sum_with_range donde le pasamos dos argumentos (números enteros)
y luego esos mismos argumentos son utilizados dentro de la función nativa range para obtener un rango entre dos números e iterar sobre ese rango para que cada
ciclo se sume el número del ciclo al resultado actual de la suma (ej. range(1, 10) = 1 + 2 + 3 + 4 + 5 ... + 10)

En la segunda parte tenemos dos funciones para crear un "Hola <nombre>. La primera sólo retorna un "hello" y la función se llama hello. La segunda función 
recibe un parámetro llamado name y cuando le pasamos el argumento (algún string en vez de la variable name) se concatena al resultado del llamado de la
función hello almacenado en una variable (ver línea 21)
"""