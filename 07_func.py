"""
EN - In this section we will be talking about functions. Basically, as in any programming language, functions are created when you need to reuse part of
your code a lot of times inside your project; then you wrap this parts of code inside a function, so you don't need to rewritte everything again.
The key word to define a function is the word "def" followed by the name of the function and below them the instructions of code that you want to be executed
as the following example shows

ES - En esta parte estaremos hablando acerca de las funciones. Básicamente, como en cualquier lenguaje de programación, las funciones son creadas cuando
se necesita reutilizar una sección de código muchas veces dentro de un proyecto; entonces se envuelven estos fragmentos dentro de una función, de manera que
no tenga que escribirse muchas veces lo mismo.
La palabra clave para definir una función es la palabra "def" seguida del nombre de la función y debajo de ellas las instrucciones de código que deben ser
ejecutadas como muestra el siguiente ejemplo
"""
def my_print():
    print("This is my custom print function")

my_print()

"""
EN - As you can see, we use the word 'def' followed by a function name (could be anyone you want, except the native functions of python like print, count, 
upper, etc), just like this def my_function_name(): Below this you can write the instructions that you want to be executed when you call that function; 
in this case we used the native function print from python to show the message "This is my custom print function" on the output screen. Finally, to call 
the function you just need to write the function's name followed by a parenthesis just like you can see in line 16.

But you can do more with function. As in other programming languages, you can send parameters as variables in order to make sure about the working 
of your code. For example, the python-native function print won't work if you don't send a parameter of type string inside the (). We can do the same 
with our functions, like you can see in the following example

ES - Como se puede ver, se utiliza la palabra 'def" seguida por un nombre de función (puede ser el nombre que quieras, menos los de las fumciones nativas de
python como print, count, upper, etc), de esta manera def nombre_funcion(): Debajo de esto se ponen las instrucciones que se ejecutarán cada vez que se llame
esa función; en este caso utilizamos la función nativa de python print para mostrar el mensaje "This is my custom print function" en la pantalla de salida. 
Finalmente, para llamar la función, sólo se necesita escribir el nombre de la función seguido de un paréntesis como se puede ver en la línea 16.

Pero no es todo lo que se puede hacer con las funciones. Como en otro lenguajes de programación, puedes enviar parámetros como variables para asegurar el
correcto funcionamiento de tu código. Por ejemplo, la función nativa de python "print", no funcionará si no envías un parámetro de tipo string dentro de los
(). Podemos hacer lo mismo con nuestras funciones, como lo veremos en el siguiente ejemplo
"""
def addition(a, b):
    print(a + b)

addition(3, 5)
addition('Hello', 'Juanvi')
# addition('Juanvi', 4) --> ERROR
addition('Juanvi', str(4)) 

"""
EN - The example above is an addition function. It needs 2 parameters to execute the operation. In python the + operator allows you to add two numbers or
concat two strings, so in this function you can send numbers or strings and it will work 
Warning: You can't use a number and a string as parameters unless you convert the number to string. 
For example if I call the function with the example of the line 40 the output will be the int number 8 (the addition of 3 and 5 that were the nums used as params).
If I call the function with the example of the line 41 the output will be HelloJuanvi
If I use the commented line 42 the output will be an error cause you can't concatenate strings with numbers.
If I use the line 43, where I converted the number to a string, the output will be Juanvi4

Just as a final comment I can call a function inside other function if is needed. The next example shows that 

ES - El ejemplo de arriba es un ejemplo de una función de suma. Necesita dos parámetros para ejecutar la operación. En python el operador + permite sumar
dos números o concatenar dos strings, así que en esta función puedes enviar strings o números y funcionará igual.
Advertencia: No puedes utilizar como argumentos un número y una string juntas a menos que conviertas el número a string
Por ejemplo, si llamo la función con el ejemplo de la línea 40 obtendré una salida del número entero 8 (la suma de 3 y 5 que puse como parámetros de entrada)
Si llamo a la función como en la línea 41 tendré una salida de la string "HelloJuanvi"
Si llamara la función como en la línea 42 tendría un error porque no puedo sumar strings y números de forma directa
Si llamo la función como en la línea 43 obtendré una salida de la string "Juanvi4"

Cómo comentario final se puede llamar una función dentro de otra función si se necesitara. El siguiente ejemplo es muestra de ello:
"""

def my_print(text):
    print(text * 2)

def suma(a, b):
    my_print(a + b)

suma(5, 6)

"""
EN - In the last excersise you can see that we have 2 functions. The first one is a custom made print wich prints a text (given as an argument in the function
parameters) 2 times. The second function is a classic addition func where you must give 2 numbers as arguments to be added and print the result of that operation.
The important thing here is that you can pass the custom print function inside the addition function and obtain a different result that you would get using the
normal print. But the point is that you can call functions inside other functions to do more complex things in your applications.

ES - En el último ejercicio se puede ver que tenemos dos funciones. La primera es una función de print propia que imprimirá cualquier texto que se pase como
argumento en los parámetros de la función, 2 veces. La segunda función es una función clásica de suma que recibe dos argumentos y luego los suma para imprimir
el resultado de esa operación. Lo importante aquí es que puedes pasar la función propia de print dentro de la función de suma obteniendo un resultado diferente
al que obtendrías usando un print normal, pero el punto es que puedes utilizar una función dentro de otras para hacer cosas más complejas en tus aplicaciones
"""