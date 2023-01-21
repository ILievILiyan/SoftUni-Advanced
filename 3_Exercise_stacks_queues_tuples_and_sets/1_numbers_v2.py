set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())

dict_functions = {
    'Add First': lambda x: [set1.add(el) for el in x],
    'Add Second': lambda x: [set2.add(el) for el in x],
    'Remove First': lambda x: [set1.discard(el) for el in x],
    'Remove Second': lambda x: [set2.discard(el) for el in x],
    'Check Subset': lambda: print(True) if set1.issubset(set2) or set2.issubset(set1) else print(False)
}

num_of_lines = int(input())
for _ in range(num_of_lines):
    action1, action2, *numbers_as_string = input().split()
    numbers = [int(x) for x in numbers_as_string]
    cmd = action1 + " " + action2

    if numbers:
        dict_functions[cmd](numbers)
    else:
        dict_functions[cmd]()

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")
