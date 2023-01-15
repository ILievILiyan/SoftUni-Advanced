num_of_names = int(input())

names = set()

for _ in range(num_of_names):
    current_name = input()
    names.add(current_name)

[print(name) for name in names]
