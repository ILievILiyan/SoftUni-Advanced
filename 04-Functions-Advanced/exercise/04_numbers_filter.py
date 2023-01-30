def even_odd_filter(**kwargs):
    total_numbers_filtered = {}

    for command, numbers in kwargs.items():
        filtered_numbers = []

        for number in numbers:
            filter_numbers = (
                    (command == CONSTANT_EVEN and number % 2 == 0) or
                    (command == CONSTANT_ODD and number % 2 != 0)
            )
            if filter_numbers:
                filtered_numbers.append(number)

        total_numbers_filtered[command] = filtered_numbers

    sorted_total_numbers_filtered = dict(sorted(total_numbers_filtered.items(), key=lambda x: -len(x[1])))

    return sorted_total_numbers_filtered


CONSTANT_EVEN = 'even'
CONSTANT_ODD = 'odd'

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
