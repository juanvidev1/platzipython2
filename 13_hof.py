"""
EN - Here we are going to talk about the High Order Functions. Basically this means that we can send a function a
as a param of another function b and execute the function a inside the function b logic. Let's see some examples 
ahead

ES - Aquí vamos a hablar acerca de las High Order Functions. Básicamente esto significa que podemos enviarle como
parámetro una función a a una función b y ejecutar la función a dentro de la lógica de la función b. Veamos algunos
ejemplos
"""
# Taking a basic increment function again as a base
def increment(x): # It receives a parameter // Recibe un parámetro
    return x + 2 # Does an operation with the parameter and return a result // Hace operaciones con el param y devuelve un resultado

# We call the function into a var with the respective argument // Invocamos la función en una variable con el respectivo argumento
result = increment(4)
# We print the result // Imprimimos el resultado
print('Este es el resultado de increment: ' + str(result)) # It should be 6 (from the operation 4 + 2) // Debería ser 6 (de la operación 4 + 2)

# Now we create a HOF that will receive the increment function as a param // Ahora crearemos una HOF qure recibirá la función increment como parámetro
def big_function(x, func):
    return x + func(x) # You execute the function here, not in params // Ejecutas la función aquí, no en los parámetros

# Calling the HOF function // Invocando la función HOF
result = big_function(4, increment) # Just put the name of the function, without parenthesis // Sólo pon el nombre de la función, sin paréntesis
print('Este es el resultado de la HOF function: ' + str(result))

"""
EN - As you can see, this is the way the High Order Functions (HOF functions) works. It is important to note
that you just should write the function name as a param or as an armgument, but not execute them in that call
or you will get an error:
    def high_order_function(x, func(x)) --> This is wrong when you create the HOF function
    result = high_order_function(x, func(x)) --> This is wrong when you call the function

But the most advantage with this is the combination of HOF with lambdas as we will see in the next examples

ES - Como puedes ver, esta es la manera en que las funciones HOF (High Order Functions) trabajan. Es importante
anotar que sólo debes escribir el nombre de la función cuando lo pases como parámetro o argumento, pero no ejecutar
la función en ese llamado o tendrás un error:
    def high_order_function(x, func(x)) --> Esto está mal cuando defines la función
    result = high_order_function(x, func(x)) --> Esto está mal cuando invocas la función

Pero la ventaja más grande es cuando combinas HOF con lambdas como veremos en los siguientes ejemplos
"""
# First define a simple lamda function
increment_v2 = lambda x : x + 1
result = increment_v2(3)
print('Este es el resultado de increment lambda: ' + str(result))

# Now we can define a HOF function with lambda too
big_function_v2 = lambda x, func : x + func(x) # The function is executed in the return (after the : statement)
result = big_function_v2(1, increment_v2) # The argument function is just named, not executed
print('Este es el resultado de HOF lamda: ' + str(result))

"""
EN - You could think that save the lambda into a variable is necessary, but let me tell you that you even don't
need to save the lamda function as the following example shows:

ES - Podrías pensar que es necesario guardar la función lambda en una variable, pero déjame decirte que no necesitas
guardar la lambda como muestra el siguiente ejemplo:
"""
# Create the HOF function and pass the lambda directly
big_function_v3 = lambda x, func : 5 + func(x) # The HOF is defined as always

# The calling of the HOF is the advantage
result = big_function_v3(2, lambda x : x + 1)
print('Este es el resultado de una función lambda que incrementa en 1 en el llamado de la HOF: ' + str(result))
result = big_function_v3(2, lambda x : x * 5)
print('Este es el resultado de una función lambda que multiplica por 5 en el llamado de la HOF: ' + str(result))

"""
EN - As you can see the best advantage of this combination between lambdas and HOF is that you can make a function
argument dynamic just using the lambdas directly without defining a whole function before; you have your function
on demand hehehe

ES - Como puedes ver la mejor ventaja de esta combinación de lambdas y HOF es que puedes hacer una función como
argumento dinámica utilizando sólo lambdas directamente sin necesidad de definir toda una función antes; tienes
tus funciones bajo demanda jejeje
"""