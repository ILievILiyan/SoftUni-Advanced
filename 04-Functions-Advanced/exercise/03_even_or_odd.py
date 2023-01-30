def even_odd(*args):
    command = args[-1]
    numbers = [int(args[x]) for x in range(len(args) - 1)]
    filtered_numbers = []

    for number in numbers:
        filter_numbers = (
            (command == CONSTANT_EVEN and number % 2 == 0) or
            (command == CONSTANT_ODD and number % 2 != 0)
        )
        if filter_numbers:
            filtered_numbers.append(number)

    return filtered_numbers



CONSTANT_EVEN = 'even'
CONSTANT_ODD = 'odd'

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

