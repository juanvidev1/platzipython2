"""
EN - Now we're going to learn how to return multiple values from a function.

ES - Ahora vamos a aprender cómo retornar múltiples valores de una función
"""
def find_volume(len, wid, dep):
    return len * wid * dep

result = find_volume(5, 3, 7)
print(result) # You will get 105 as a result // Obtendrás 105 como resultado

"""
EN - We should be very carefully with the parameters we define for a function. In the example above if I try to execute the find_volume function without
passing arguments (if I call the function like this find_volume()) I will get an error because I defined that the function only will work if it has those
arguments; so if it's called with empty values the code will break and you will get an error that the arguments are missing. You can solve this giving default
values to the parameters of the function so it can work as arguments as the next example shows:

ES - Deberíamos ser muy cuidadosos con los parámetros que definimos para una función. En el ejemplo de arriba si trato de llamar la función find_volume sin
pasarle los argumentos (o sea si llamo la función así --> find_volume()) tendré un error porque decidí que la función sólo trabajará si tiene esos argumentos;
así que si la llamé con valores vacíos el código se romperá y obtendré un error que indica que faltan los argumentos. Esto se puede resolver dándole valores
por defecto a los parámetros de la función para que puedan servir simultáneamente como argumentos como en el ejemplo siguiente:
"""
def find_volume(len=1, wid=2, dep= 3):
    return len * wid * dep

result = find_volume()
print(result) # You will get 6 as a result // Obtendrás 6 como resultado

"""
EN - As you can see, I defined now that the parameters has a default value that will be used if I don't pass any arguments to the function and it still works.
But you can also define wich parameters will have a default value and wich needs to be setted by the user like the example below
Warning: You should add the default value argument as the last one or you will get an error.

def find_volume(len, dep, wid=10):
    return len*wid*dep

result=find_volume(2, 3)
print(result) # You will get 60

Also you can set just one of the values and use the default of the others, like the example of calling in line 55

ES - Como puedes ver, definí ahora que los parámetros tengan un valor por defecto que será utilizado en caso de que no se le pase ningún argumento a la función
y aún así seguirá trabajando. Pero también puedes definir qué parámetros van a tener un valor por defecto y cuáles deben tener un valor asignado por el usuario
como en el ejemplo de abajo
Advertencia: Deberías poner el argumento con valor por defecto al final de los argumentos o te generará error.

def find_volume(len, dep, wid=10):
    return len*wid*dep

result=find_volume(2, 3)
print(result) # Obtendrás 60

También puedes establecer sólo uno de los valores y utilizar el valor por defecto de los otros parámetros, como en el ejemplo de invocación de la línea 55
"""
result = find_volume(wid=8)
print(result) # You will get 24 as a result // Obtendrás 24 como resultado

"""
EN - Finally you can return more than one value from a function. You can do this using "," to return more than one value just like this:
return <value1>, <value2>, <value3>

ES - Finalmente puedes retornar más de un valor de una función. Puedes hacer esto utilizando "," para devolver más de un valor justo así:
return <value1>, <value2>, <value3>
"""
def square_vol(len=1, wid=1, dep=1):
    var1 = len * wid * dep
    var2 = 'Hello'
    return wid, var1, var2 # When you print this you will get a tuple with (wid, var1, var2) // Cuando imprimas esto tendrás una tupla con (wid, var1, var2)

result = square_vol(3, 5, 3)
print(result) # You wil get (5, 45, 'Hello') as a result // Obtendrás (5, 45, 'Hello') como resultado