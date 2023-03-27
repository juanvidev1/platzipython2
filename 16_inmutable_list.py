"""
EN - Now we are going to see how to keep the original items list and creating a new one with the tax attribute

ES - Ahora vamos a ver cómo mantener la lista original sin cambios y creat una nueva con el atributo de impuesto
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

def add_taxes(items):
    new_items = items.copy() # This line creates a copy of the original list and stores it in the new_items list
    # items['taxes'] = items['price'] * .19 # In this line is where the modification to the original items list occurs
    new_items['taxes'] = new_items['price'] * .19 # This works inside the new_items list without changing the original items list
    return new_items

taxes_list = list(map(add_taxes, items)) # The function creates the new list so we can still iterate the original items list without modifying it

print('New list')
print(taxes_list) # This is the new list generated with map function and with taxes attribute included
print('Old list')
print(items)

