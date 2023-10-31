def even_numbers(list_of_numbers):
    for el in list_of_numbers:
        if el % 2 == 0 and el != 0:
            print(el)
numbers = list(range(10))
even_numbers(numbers)
