num_of_names = int(input())
even_set = set()
odd_set = set()
current_row = 0

for _ in range(num_of_names):
    name = input()
    current_row += 1

    sum_name = 0
    sum_name += sum([ord(ch) for ch in name])
    sum_name /= current_row

    if int(sum_name) % 2 == 0:
        even_set.add(int(sum_name))
    else:
        odd_set.add(int(sum_name))

sum_even = sum(even_set)
sum_odd = sum(odd_set)

if sum_odd == sum_even:
    set_to_print = odd_set.update(even_set)
elif sum_odd > sum_even:
    set_to_print = odd_set.difference(even_set)
else:
    set_to_print = odd_set.symmetric_difference(even_set)

print(f'{", ".join(map(str, set_to_print ))}')