"""
EN - In this excersise we will learn about CRUD operations over data sets. Here we can see how to Create, Read, Update and Delete elements from a data set

ES - En este ejercicio aprenderemos sobre las operaciones CRUD sobre los conjuntos. Aquí veremos cómo Crear, Obtener, Actualizar y Eliminar 
elementos de un conjunto
"""
set_countries = {'Col', 'Mex', 'Bol'}

"""
EN - As other data structures in programming languages, you can do a lot of things with sets. The first one is show the length of the set 
(the number of elements that the set contains). You can make this with the len() method of python

ES - Como en otras estructuras de datos en los lenguajes de programación, puedes hacer muchas cosas con los conjuntos. 
Una de las primeras es averiguar el tamaño del conjunto (el número de elementos que contiene). Puedes hacer esto con el método len() de python
"""
size = len(set_countries)
print(size)

"""
EN - Another interesting thing, and really easy to do, is search for an element that could be inside the set. You can do that using the following sintax:
<element> in <set_where_you_want_to_search>. If the element is in the set, the output of the code will be True, if not the output will be False. 
The following example can make this clear:

ES - Otra cosa interesante, y realmente fácil de hacer, es buscar un elemento que podría estar dentro del conjunto. Puedes hacer esto utilizando la sintaxis:
<elemento> in <conjunto_donde_quieres_buscar>. Si el elemento se encuentra dentro del conjunto la salida del código será True, si no, será False.
El siguiente ejemplo puede aclarar esto:
"""
find_element = 'Col' in set_countries
find_element_2 = 'Pe' in set_countries
print(find_element)
print(find_element_2)

"""
EN - You can add elements to the set using the method add. This is the sintax: <set_which_you_want_to_add_element>.add(<element_you_want_to_add>).
Warning: If you try to add an element that already is in the set, the code will work, but the element will continue being unique in the set.
The following example shows how this works

ES - Puedes agregar elementos a un conjunto utilizando el método add. Esta es la sintaxis: 
<conjunto_al_que_quieres_agregar_el_elemento>.add(<elemento_que_quieres_agregar>).
Advertencia: Si tratas de agregar un elemento que ya esté en el conjunto, el código va a funcionar, pero el elemento va a seguir siendo único en el conjunto
El siguiente ejemplo muestra como funciona esto:
"""
set_countries.add('Pe')
print(set_countries)
set_countries.add('Col')
print(set_countries)

"""
EN - As the same way you add elements, you could be able to update sets. But the idea of update here is used to add more elements to the set. In this way
I can add other data structures to an existing set, for example another set of elements that want to be added to my actual set. The sintax is like this:
<principal_elements_set>.update(<data_structure_that_want_to_be_added>). The next example will show how this works

ES - De la misma manera en que agregas elementos a un conjunto, puedes actualizarlo. Aunque la idea de actualizar es agregar más elementos a un conjunto principal.
En ese orden de ideas puedes agregar otras estructuras de datos a un conjunto ya existente, por ejemplo, puedes agregar un conjunto de datos al conjunto que ya
tienes. La sintaxis sería algo como esto:
<conjunto_existente>.update(<estructura_de_datos_que_quieres_agregar>). El siguiente ejemplo muestra cómo funciona esto
"""
set_countries.update({'Ar', 'Ecu', 'Bol'})
print(set_countries)
set_countries.update(['Ur', 'Cl'])
print(set_countries)

"""
EN - Now we can se the elements delete from a set. You have 3 options here: 
    1. Use the remove method. This method allows to delete an element, but if the element doesn't exist in the list, your software or app will crash 
    because the element is not present in the set. The sintax is very similar to the add and update methods:
    <set_of_elements_you_already_have>.remove<element_you_want_to_delete>

    2. Use the discard method. This method is a little bit better than remove because it does the same thing of remove, but if the element you're trying to
    delete doesn't exist the software or app won't break, just the method won't delete anything because that element are not inside the set. The sintax is:
    <set_you_already_have>.discard(<element_you_want_to_delete>)

    3. Use the clear method. This method delete all the elements from the set. The sintax is like this:
    <set_you_want_to_delete>.clear()
    This will return an empty set.

ES - Ahora veremos como puedes eliminar elementos de un conjunto. En este caso tienes 3 opciones:
    1. Utilizar el método remove. Este método te deja eliminar un elemento del conjunto, pero si el elemento no existe en el conjunto, tu programa o aplicación
    va a fallar porque el elemento no está presente en el conjunto. La sintaxis es muy similar a los métodos de add y update:
    <conjunto_de_elementos_que_ya_tienes>.remove(<elemento_que_quieres_eliminar>)

    2. Utilizar el método discard. Este método también funciona para eliminar elementos; sin embargo es un poco mejor, ya que si el elemento que quieres eliminar
    no existe en el conjunto, discard no va a romper tu programa o app, pero tampoco va a eliminar nada, simplemente no va a eliminar nada porque lo que quieres
    quitar del conjunto no existe dentro de el. La sintaxis es la siguiente:
    <conjunto_de_elementos_que_ya_tienes>.discard(elemento_que_quieres_eliminar)

    3. Utilizar el método clear. Este método eliminará todo el contenido del conjunto. La sintaxis es de la siguiente manera:
    <conjunto_de_elementos_a_eliminar>.clear()
    Esto devolverá un conjunto vacío
"""
# Remove example
set_countries.remove('Cl')
print(set_countries)
"set_countries.remove('Ang')" #This line will break the code because Ang doesn't exist in the set / Esta línea romperá el código porque Ang no está en el conjunto

# Discard example
set_countries.discard('Ur')
print(set_countries)
set_countries.discard('Arg') #This line won't break the code even when Arg doesn't exist in set // Esta línea no romperá nada aunque Arg no está en el conjunto
print(set_countries) # Thats why here we can put the print and with remove not. // Por eso aquí si podemos poner el print y con remove no.

# Clear example
set_countries.clear()
print(set_countries)