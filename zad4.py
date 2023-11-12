def numbers_sum(first: int, second: int, third: int) -> bool:
    if first + second >= third:
        return True
    else:
        return False

print(numbers_sum(1,4,10))
