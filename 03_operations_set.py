"""
EN - In this class we will see how to do operations with sets.

ES - En esta clase veremos como hacer operaciones con los conjuntos
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