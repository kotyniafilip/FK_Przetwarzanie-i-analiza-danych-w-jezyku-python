def x2numbers(list_of_numbers):
    numbers = []
    for el in list_of_numbers:
        numbers.append(el * 2)
    return numbers
list = [5,10,15,20,25]
numbers = x2numbers(list)
print(numbers)