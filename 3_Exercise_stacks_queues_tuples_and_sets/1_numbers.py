def add_items(set_to_add, items_to_add):
    set_to_add = set_to_add.union(items_to_add)
    return set_to_add


def remove_items(set_to_remove, items_to_remove):
    set_to_remove = set_to_remove.difference(items_to_remove)
    return set_to_remove


set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}

num_of_lines = int(input())

for _ in range(num_of_lines):
    command = input().split()

    action, set_to_change, numbers = command[0], command[1], command[2:]
    numbers = set(int(x) for x in numbers)

    if action == "Check" and set_to_change == "Subset":
        print(set1.issubset(set2) or set2.issubset(set1))
    elif action == 'Add':
        if set_to_change == "First":
            set1 = add_items(set1, numbers)
        elif set_to_change == "Second":
            set2 = add_items(set2, numbers)
    elif action == "Remove":
        if set_to_change == "First":
            set1 = remove_items(set1, numbers)
        elif set_to_change == "Second":
            set2 = remove_items(set2, numbers)

if set1:
    print(", ".join(map(str, sorted(set1))))
if set2:
    print(", ".join(map(str, sorted(set2))))
