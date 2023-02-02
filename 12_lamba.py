"""
EN - Now we're gonna learn about lambda functions. Basically this kind of function is a short way to create
simple functions different from the usual way:
def <function_name>(<param>):

    <operation logic with the param>

    return <operation_result>

The example shows this better

ES - Ahora vamos a aprender sobre las funciones lambda. Básicamente este tipo de función es una manera corta de
crear funciones simples diferente a la usual:
def <nombre_funcion>(<parámetro>):

    <lógica operacional con el parámetro>

    return <resultado_operación>

El ejemplo muestra esto mejor
"""
def increment(x):
    return 'Este retorno es de una función tradicional: ' + str(x + 1)

result = increment(10)
print(result)

"""
EN - Now we can 'convert' that traditional function into a lambda function using the following sintax:
    <function_name> = lambda <arguments*> : <expected_return>

    The function calling is the same:
    <function_name>(<argument>)

The example shows how this works

    * The arguments are the values that are assigned to the params of a normal function
        example
        def myFunction(x): --> This is a parameter
            return x + 1
        
        # Function Calling
        myFunction(10) --> In this case this is an argument because the param x has a value

ES - Ahora vamos a 'convertir' esa función tradicional en una función lambda utilizando la siguiente sintaxis:
    <nombre_funcion> = lambda <argumentos*> : <retorno_esperado>

El ejemplo muestra cómo funciona esto

    * Los argumentos son los valores que se le asignan a los parámetros de una función normal
        ejemplo
        def myFunction(x): --> En este caso es un parámetro
            return x + 1
        
        # Se llama la funcióm
        myFunction(10) --> En este caso ya es un argumento por que el parámetro x ya tiene valor

"""
increment_v2 = lambda x : 'Este retorno es de una función lambda: ' + str(x + 1)
result = increment_v2(15) # The func calling is the same // El llamado de la función es el mismo

print(result)