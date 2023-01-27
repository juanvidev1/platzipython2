"""
EN - Now we're gonna talk about variables scopes. When you develop something your vars will have different scope levels: local, enclosing, global and built-in 
(where local is the smallest scope and built-in the biggest scope you can set). A global variable is that one that you define in your code and can be used in
any part of your file as you can see in the variable of the line 10

ES - Ahora vamos a hablar del scope de las variables. Cuando desarrollas algo tus variables tendrán diferentes niveles de scope: local, enclosing, global y
built-in (donde local es el scope más pequeño y built-in el más grande que puedes setear). Una variable global es una variable que puedes definir en tu código
y utilizarla en cualquir parte de tu archivo como ves en la variable de la línea 10
"""
price = 100 # This is a global variable // Esta es una variable global
# Doesn't matter where I call it, it will exist in any part of the code // No importa donde la llame, siempre existirá en cualquier parte del código

"""
EN - A local variable is defined inside a function and only has sense and will exist inside the function. If you try to call that variable outside the function
you will get an error because it doesn't exist outside of the func environment. Also you can have global and local variables with the same name and both will
be completely different and if you create a global variable it will be other than a variable with the same name but defined inside a function. For example if
we take the price var from the line 10, you can't do this inside a function

def increment():
    price = price + 10
    print(price)

increment() --> This call will return you an error because the function will not understand what is price because that variable is not recognized inside the funct
environment

The correct way starts in the line 41

ES - Una variable local es definida dentro una función y sólo tiene sentido y existirá dentro de la función. Si tratas de llamar la variable fuera de la función
tendrás un error porque no existe fuera del ambiente de dicha función. También puedes tener variables locales y globales con el mismo nombre y ambas serán
diferentes e independientes una de otra. Por ejemplo, si tomamos la variable price de la línea 10, no puedes hacer esto dentro de una función

def increment():
    price = price + 10
    print(price)

increment() --> Esta invocación retornará un error porque la función no entenderá qué es "price" porque la variable, aunque existe globalmente, no es reconocida
en el ambiente local de la función

La forma correcta está a partir de la línea 41
"""
def increment():
    price = 200 # Local variable defined inside the function and != from global "price" // Variable local definida dentro de la functión y != a "price" global
    price = price + 10
    print(price)

print(price) # You will get a result of 100 (global price value) // Obtendrás un resultado de 100 (valor de price global)
increment() # You will get 210 result (local price + 10) // Obtendrás un resultado de 210 (price local + 10)

"""
EN - But, what if we want to use the global var inside a function? We can do it if we define an argument with a default value with the global variable just like
this

ES - Pero, ¿y si quieremos utilizar la variable global dentro de una función? Lo podemos hacer si definimos un argumento con el valor por defecto de la variable
global así
"""
def increment_2(price=price):
    price = price + 10
    return price

result = increment_2()
print(result) # You will get a 110 result (global price + 10) // Obtendrás un resultado de 110 (price global  + 10)