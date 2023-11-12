def even_number(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

liczba = even_number(6)

if liczba:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


