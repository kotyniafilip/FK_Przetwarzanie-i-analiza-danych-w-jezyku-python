def second_numbers(list_of_numbers):
    for i in range(0, len(list_of_numbers), 2):
        print(list_of_numbers[i])

numbers = list(range(10))
second_numbers(numbers)
