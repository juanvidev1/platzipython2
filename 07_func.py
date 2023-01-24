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
EN - The example above is an addition function. It needs 2 parameters to execute the operation. In python the + operation allows you to add two numbers or
concat two strings, so in this function you can send numbers or strings and it will work but you can't use a number and a string as parameters unless you
convert the number to string. 
For example if I call the function with the example of the line 40 the output will be the int number 8.
If I call the function with the example of the line 41 the output will be HelloJuanvi
If I use the commented line 42 the output will be an error cause you can't concatenate strings with numbers.
"""