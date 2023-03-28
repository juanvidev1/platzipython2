def multiply_numbers(numbers):
    # Escribe tu solución 👇
    return list(map(lambda i: i*2, numbers))

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)