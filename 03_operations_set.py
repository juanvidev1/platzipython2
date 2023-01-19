"""
EN - In this class we will see how to do operations with sets. This operations only works with sets with common elements.

ES - En esta clase veremos como hacer operaciones con los conjuntos. Estas operaciones sólo funcionan con elementos en común entre conjuntos 
"""
set_a = {'Col', 'Mex', 'Bol'}
set_b = {'Pe', 'Bol'}

"""
EN - For the first operation we will see union. This operation allows to combine the elements of two separate sets, but it maintain the unique elements per set
rule. The sintax is like this:
<set_a>.union(<set_b>) --> You can save this inside a variable; the following example will make it clear

ES - Para la primera operación veremos la unión. Esta operación permite combinar elementos de dos conjuntos separados, pero mantiene la regla de elementos únicos
por conjunto. La sintaxis es algo como esto:
<conjunto_a>.union(<conjunto_b>) --> Esto se puede guardar en una variable; el siguiente ejemplo lo hará más claro
"""
set_c = set_a.union(set_b)
print(set_c)

"""
EN - You can also do the union for sets in other ways. For example the sintax <set_a> | <set_b> works in the same way that the method union. The example shows how

ES - También puedes unir conjuntos de otras maneras. Por ejemplo la sintaxis <conjunto_a> | <conjunto_b> funciona de la misma manera que el método union.
El ejemplo a continuación muestra como
"""
set_c = set_a | set_b
print(set_c)

"""
EN - The next operation is the intersection. This operation shows wich elements of two sets are present in both of them or is common to both sets.
The sintax is very similar to the other ways to work with sets: <set_a>.intersection(<set_b>) 
You can also use a math operator to do the operation like this: <set_a> & <set_b>

ES - La siguiente opración es la intersección. Esta operación muestra cuáles elementos de dos conjuntos están presentes o son comunes en ambos conjuntos
La sintaxis es muy similar a lo que hemos visto para trabajar con conjuntos: <conjunto_a>.intersection(<conjunto_b>)
De igual forma podemos utilizar un operado aritmético para la operación de esta manera: <conjunto_a> & <conjunto_b>
"""
set_c = set_a.intersection(set_b)
print(set_c)

set_c = set_a & set_b
print(set_c)

"""
EN - Now we are go to talk about the difference operation. Basically consists in remove the common elements between a set_a and a set_b 
and create a "new" set_c with the result of this sustraction.
The sintax is: <set_a>.difference(<set_b>)
The example below explains better this

ES - Ahora vamos a hablar acerca de la operación de diferencia. Básicamente consiste en remover los elementos comunes entre un 
conjunto_a y un conjunto_b para crear un "nuevo" conjunto_c con el resultado de esa resta.
La sintaxis es: <conjunto_a>.difference(<conjunto_b>)
El ejemplo de abajo explica mejor esto  
"""
set_c = set_a.difference(set_b)
print(set_c)
"""
EN - Also has a math operator as other operations between sets

ES - También tiene operadores matemáticos como las otras operaciones entre conjuntos
"""
set_c = set_a - set_b
print(set_c)

"""
EN - Finally we're going to talk about Symmetric Difference. Here we remove all the common elements of both sets (a, b) 
but those wich are not common to both sets (a, b).
Sintax: <set_a>.symetric_difference(<set_b>)
Operator syntax: <set_a> ^ <set_b> 

ES - Finalmente hablaremos de la diferencia simétrica. Aquí se remueven todos los elementos comunes de los conjuntos (a, b) excepto aquellos elementos 
que no sean comunes a ambos conjuntos (a, b).
Sintaxis: <conjunto_a>.symetric_difference(<conjunto_b>)
Sintaxis con operador: <conjunto_a> ^ <conjunto_b>
"""
set_c = set_a.symmetric_difference(set_b)
print(set_c)
set_c = set_a ^ set_b
print(set_c)