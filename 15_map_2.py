"""
EN - We also can use the map function with dictionaries lists. That's the common use case we can found when we are
working with map function

ES - También podemos usar la función map con listas de diccionarios. Este es el caso de uso más común cuando estamos
trabajando con la función map en contextos más profesionales
"""

items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 120
    },
    {
        'product': 'chaqueta',
        'price': 200
    },
    {
        'product': 'medias',
        'price': 40
    }
]

#products = list(map(lambda items: items, items))
price = list(map(lambda items: items['price'], items))

#print(products) 
#Result = [{'product': 'camisa', 'price': 100}, {'product': 'pantalones', 'price': 120}, {'product': 'chaqueta', 'price': 200}, {'product': 'medias', 'price': 40}]
print(price)

"""
EN - In the last case we extracted the price from each dictionary item in the list. But we could transform this to 
include more data in each dictionary object. For example, what if we need to add a taxes field in the dictionary 
that brings the tax calculation for the price of each item? Let's see how this works

ES - En el último caso obtuvimos sólo el precio de cada item dentro de la lista. Pero podríamos tranformar esto
para incluir más data en cada diccionario dentro de la lista. Por ejemplo, qué tal si necesitamos añadir un campo
en cada item que contenga un cálculo de los impuestos para el precio de cada producto? Vemos cómo trabaja esto
"""


# In this case we need to create a new function. Here we can't work with lamba func because we must set a complex logic to add the new field in the dictionary
def add_taxes(items):
    items['taxes'] = items['price'] * .19
    return items

#Here we use the map function as always. The first argument will be the function of the line 46 and the second argument will be the list or iterable item
taxes_list = list(map(add_taxes, items))
print(taxes_list)
# The print will have the new list with the field with the calculated tax value for each item in the original list