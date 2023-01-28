num_of_lines = int(input())
set_with_elements = set()

for _ in range(num_of_lines):
    current_line = input().split()
    set_with_elements.update(current_line)

for el in set_with_elements:
    print(el)