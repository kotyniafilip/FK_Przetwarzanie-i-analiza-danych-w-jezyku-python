def x2numbers(list_of_numbers):
    numbers = []
    for el in list_of_numbers:
        numbers.append(el * 2)
    return numbers

my_list = [5, 10, 15, 20, 25]
result_numbers = x2numbers(my_list)
print(result_numbers)
