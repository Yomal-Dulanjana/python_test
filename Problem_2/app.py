def square_evens(numbers: list) -> list:
    return [x**2 for x in numbers if x % 2 == 0]

print(square_evens([1, 2, 3, 4, 5]))
